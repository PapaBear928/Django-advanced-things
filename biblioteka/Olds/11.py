from django.db import models

class Autor(models.Model):
    imie = models.CharField(max_length=20, blank=False)
    nazwisko = models.CharField(max_length=20, blank=False)
    data_urodzenia = models.DateField(null=True, blank=True, default=None)

    def __str__(self):
        return self.imie + " " + self.nazwisko

#aded: lesson nr 11 = Choices
class Gatunek():
    UNKNOWN = 0
    FANTASY = 1
    DRAMA = 2
    ACTION = 3

    GATUNKI = (
        (UNKNOWN, 'Unknown'),
        (FANTASY, 'Fantasy'),
        (DRAMA, 'Drama'),
        (ACTION, 'Action'),

    )
# added: lesson nr12 = MANAGERS
class NoweManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(rok_wydania__gte=2000)

class StareManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(rok_wydania__lte=2000)


class Ksiazka(models.Model):
    tytul = models.CharField(max_length=50, blank=False)
    rok_wydania = models.IntegerField(blank=False)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, related_name='ksiazki')
#aded: lesson nr 11 = Choices
    gatunek = models.PositiveIntegerField(choices=Gatunek.GATUNKI, default=0)
    nowe = NoweManager()
    stare = StareManager()
    objects = models.Manager()



    def __str__(self):
        return self.tytul
