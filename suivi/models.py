from django.db import models





class Produit(models.Model):
    produit_nom = models.CharField("Nom de produit", max_length=100, blank=False, default='')
    client = models.CharField("Client", max_length=100, blank=False, default='')
    status = models.CharField("Status", max_length=20, blank=False, default='')

 