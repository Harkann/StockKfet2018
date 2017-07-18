from django.shortcuts import render
from .models import Produit
from django.db.models import F
from .add import *
from django.forms import modelformset_factory

def produits(request):
    return render(request, 'produits/produits.html',{})
def accueil(request):
    return render(request, 'produits/accueil.html',{})

def search_product(request):
    is_search = False
    search_query = request.GET.get('search_box', None)
    if search_query != None and search_query != "" :
        is_search = True
        try :
            produit = Produit.objects.filter(nom__startswith=search_query)
        except :
            try :
                produit = Produit.objects.filter(code_barre=search_query)
            except :
                is_search = False
    if not is_search :
        produit = None

    ProduitFormset = modelformset_factory(Produit, fields = ('nom','quantite','seuil_commande',))
    formset = ProduitFormset(request.POST or None, request.FILES or None, queryset=produit)
    if formset.is_valid():
            formset.save()
    return render(request, 'produits/search_product.html', {'form': formset, 'is_search' : is_search})

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            new_produit = form.save()
    else :
        form = ProductForm()
    return render(request, 'produits/add_product.html', {'form': form})

def add_fournisseur(request):
    if request.method == 'POST':
        form = FournisseurForm(request.POST)
        if form.is_valid():
            new_fournisseur = form.save()
    else :
        form = FournisseurForm
    return render(request, 'produits/add_fournisseur.html', {'form': form})

def courses(request):
    a_commander = Produit.objects.filter(quantite__lte=F('seuil_commande'))
    return render(request, 'produits/courses.html',{'a_commander': a_commander})

def list_produits(request):
    produits = Produit.objects.order_by('fournisseur')
    return render(request, 'produits/list_produits.html',{'produits' : produits})




