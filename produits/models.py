from __future__ import unicode_literals
from django.db import models
from django.utils import timezone

class Produit(models.Model):
    def fournisseur_default():
        return 'randomGuy'

    nom = models.CharField(max_length=50)
    prix = models.DecimalField(max_digits=10,decimal_places=2)
    code_barre = models.CharField(max_length=20,unique=True)
    quantite = models.PositiveIntegerField()
    seuil_commande = models.PositiveIntegerField()
    fournisseur = models.ForeignKey('Fournisseur',on_delete=models.PROTECT,default=fournisseur_default())

    def register(self):
        self.save()

    def __str__(self):
        return self.nom + ' ' + self.fournisseur.nom

class Fournisseur(models.Model):

    def name_default():
        return 'randomguy'

    nom = models.CharField(max_length=50,primary_key=True,default=name_default)
    numero = models.CharField(max_length=10,blank=True,null=True)
    rue = models.CharField(max_length=50,blank=True,null=True)
    ville = models.CharField(max_length=50,blank=True,null=True)
    telephone = models.CharField(max_length=10,blank=True,null=True)

    def register(self):
        self.save()

    def __str__(self):                                                               
        return self.nom

class Facture(models.Model):

    def fournisseur_default():
        return 'randomGuy'

    date = models.DateTimeField(default = timezone.now)
    fournisseur = models.ForeignKey('Fournisseur',on_delete=models.PROTECT,default=fournisseur_default())
    produit = models.ManyToManyField('Produit',limit_choices_to = {'fournisseur' : fournisseur})
    quantite = models.PositiveIntegerField()

    def register(self):
        self.save()

    def __str__(self):
        return str(self.date) + ' ' + self.fournisseur.nom

class Sortie(models.Model):
    date = models.DateTimeField(default = timezone.now)



