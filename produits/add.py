from django import forms
from .models import Fournisseur
from .models import Produit

class ProductForm(forms.ModelForm):
    class Meta:
        model = Produit
        fields = ['nom','prix', 'code_barre', 'quantite', 'seuil_commande', 'fournisseur']

class partialProductForm(forms.ModelForm):
    class Meta:
        model = Produit
        fields = ['nom','quantite','seuil_commande']



class FournisseurForm(forms.ModelForm):
    class Meta:
        model = Fournisseur
        fields = ['nom','numero','rue','ville','telephone']
