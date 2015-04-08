from django.db import models
from django.contrib.auth.models import User

class Termometr(models.Model):
    nazwa = models.CharField(max_length=20)
    datadodania = models.DateTimeField(auto_now_add=True,blank=True)
    dodanyprzez = models.ForeignKey(User)

    def __str__(self):
        return self.nazwa

class Odczyt(models.Model):
    odczyt = models.DecimalField
    termometr = models.ForeignKey(Termometr)
    data = models.DateTimeField

    def __str__(self):
        return self.odczyt