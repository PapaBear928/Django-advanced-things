from django.db import models
from .managers import KsiazkaManager
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.core.validators import MaxValueValidator
from .validators import validate_rok

class Autor(models.Model):
    imie = models.CharField(max_length=20, blank=False)
    nazwisko = models.CharField(max_length=20, blank=False)
    data_urodzenia = models.DateField(null=True, blank=True, default=None)


    def __str__(self):
        return self.imie + " " + self.nazwisko

@receiver([ pre_save], sender=Autor) ### SPOSÓB 2
def author_before_save(sender, instance, **kwargs):
    print(' Saving the author')

    our_author = Autor.objects.get(id=instance.id)
    print(our_author.imie)

@receiver([post_save], sender=Autor) ### SPOSÓB 2
def author_after_save(sender, instance, **kwargs):
    print(' Just save the author')
    print(instance.imie)
### SPOSÓB 1
#post_save.connect(author_after_save, sender=Autor)

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
    rok_wydania = models.IntegerField(blank=False, validators=[MaxValueValidator(2022)])
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, related_name='ksiazki')
#aded: lesson nr 11 = Choices
    gatunek = models.PositiveIntegerField(choices=Gatunek.GATUNKI, default=0)
    ksiazki = KsiazkaManager()
    objects = models.Manager()

    def save(self, *args, **kwargs):
       # if self.rok_wydania >2020:
       #     raise ValueError('To nie można tak')
        validate_rok(self.rok_wydania)
        super(Ksiazka,self).save(*args, **kwargs)

    def __str__(self):
        return self.tytul

    def is_modern(self):
        return True if self.rok_wydania > 2000 else False

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