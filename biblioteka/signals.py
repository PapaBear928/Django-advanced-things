from django.core.signals import request_finished
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver, Signal
from .models import Autor
import logging

autor_log = logging.getLogger('autor_log')
autor_log.setLevel(logging.DEBUG)
log_handler = logging.FileHandler('logs/autor.log')
log_handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
log_handler.setFormatter(formatter)
autor_log.addHandler(log_handler)

main_signal = Signal(['imie'])

@receiver([ pre_save], sender=Autor)
def author_before_save(sender, instance, **kwargs):
    print(' Saving the author')
    our_author = Autor.objects.get(id=instance.id)
    print(instance)
    autor_log.info("Someone create autor" + instance.imie + ""  + instance.nazwisko)

@receiver([post_save], sender=Autor) ### SPOSÓB 2
def author_after_save(sender, instance, **kwargs):
    print(' Just save the author')
    print(instance.imie)
### SPOSÓB 1
#post_save.connect(author_after_save, sender=Autor)

@receiver(request_finished)
def strona_wczytana(sender, **kwargs):
    print("Site is going ")


@receiver(main_signal)
def strona_wczytana(sender, **kwargs):
    print("Name ", kwargs.get('imie'))