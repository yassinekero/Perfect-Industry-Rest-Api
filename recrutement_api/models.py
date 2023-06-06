from django.db import models


class Demande(models.Model):
    prenom = models.CharField("Prenom", max_length=100, blank=False, default='')
    nom = models.CharField("Nom", max_length=100, blank=False, default='')
    email = models.CharField("Email", max_length=300, blank=False, default='')
    telephone = models.CharField("Telephone", max_length=50, blank=False, default='')
    occupation = models.CharField("Occupation", max_length=200, blank=False, default='')
    lienCv = models.CharField("Lien CV", max_length=1000, blank=False, default='')

    def __str__(self) -> str:
        return self.prenom
