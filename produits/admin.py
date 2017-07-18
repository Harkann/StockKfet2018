from django.contrib import admin
from .models import Produit, Fournisseur, Facture, Sortie

admin.site.register(Produit)
admin.site.register(Fournisseur)
admin.site.register(Facture)
admin.site.register(Sortie)

