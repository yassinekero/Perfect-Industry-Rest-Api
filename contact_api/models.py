from django.db import models


class Demande(models.Model):
    prenom = models.CharField("Prenom", max_length=100, blank=False, default='')
    nom = models.CharField("Nom", max_length=100, blank=False, default='')
    email = models.CharField("Email", max_length=300, blank=False, default='')
    telephone = models.CharField("Telephone", max_length=20, blank=False, default='')
    message = models.CharField("Message", max_length=2000, blank=False, default='')

    def __str__(self) -> str:
        return self.prenom