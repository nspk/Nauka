from django.db import models

class Message(models.Model):
    uzytkownik = models.CharField(max_length=30)
    email = models.EmailField()
    tresc = models.TextField()

    def __str__(self):
        return "wiadomość od {uzytkownik}".format(uzytkownik = self.uzytkownik)
