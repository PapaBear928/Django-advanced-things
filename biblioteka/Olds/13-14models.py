from django.db import models
from .managers import KsiazkaManager


class Autor(models.Model):
    imie = models.CharField(max_length=20, blank=False)
    nazwisko = models.CharField(max_length=20, blank=False)
    data_urodzenia = models.DateField(null=True, blank=True, default=None)

    def __str__(self):
        return self.imie + " " +  self.nazwisko

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


class Ksiazka(models.Model):
    tytul = models.CharField(max_length=50, blank=False)
    rok_wydania = models.IntegerField(blank=False)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, related_name='ksiazki')
#aded: lesson nr 11 = Choices
    gatunek = models.PositiveIntegerField(choices=Gatunek.GATUNKI, default=0)
    ksiazki = KsiazkaManager()
    objects = models.Manager()


    def __str__(self):
        return self.tytul


    class Meta:
        #db_table = 'coś domyślnego'
        #ordering = ['rok_wydania']
        #order_with_respect_to = 'autor'
        verbose_name = 'książka'
        verbose_name_plural = 'książki'
        unique_together = [
            ['tytul', 'rok_wydania', 'autor']
        ]
        indexes = [
            models.Index(fields=['tytul'], name='tytul_inx'),
            models.Index(fields=['tytul', 'rok_wydania'])
        ]
        permissions = [
            ('cab_update_ksiazka', "Moze zmieniac książkę")
        ]