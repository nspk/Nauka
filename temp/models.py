from django.db import models
from decimal import Decimal
from django.contrib.auth.models import User

class Termometr(models.Model):
    nazwa = models.CharField(max_length=20)
    datadodania = models.DateTimeField(auto_now_add=True,blank=True)
    dodanyprzez = models.ForeignKey(User)

    def __str__(self):
        return self.nazwa

class Odczyt(models.Model):
    odczyt = models.DecimalField(max_digits=5,decimal_places=2,default=Decimal('0.00'))
    termometr = models.ForeignKey(Termometr)
    data = models.DateTimeField(auto_now_add=True,blank=True)

    def __str__(self):
        return str(self.odczyt)