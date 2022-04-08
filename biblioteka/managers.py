from django.db import models

class KsiazkaQuerySet(models.QuerySet):
    def nowe(self):
        return self.filter(rok_wydania__gte=2000)
    def stare(self):
        return self.filter(rok_wydania__lte=2000)

#bulid a manager
class KsiazkaManager(models.Manager):
    def get_queryset(self):
        return KsiazkaQuerySet(self.model, using=self.__db)

    def nowe(self):
        return self.get_queryset().nowe()

    def stare(self):
        return self.get_queryset().stare()

# added: lesson nr12 = MANAGERS
#class NoweManager(models.Manager):
#    def get_queryset(self):
#        return super().get_queryset().filter(rok_wydania__gte=2000)

#class StareManager(models.Manager):
#    def get_queryset(self):
#        return super().get_queryset().filter(rok_wydania__lte=2000)
