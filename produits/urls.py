
from django.conf.urls import url
from . import views

urlpatterns = [
        url(r'^$',views.accueil, name='accueil'),
        url(r'^add_product',views.add_product, name='add_product'),
        url(r'^add_fournisseur',views.add_fournisseur, name='add_fournisseur'),
	url(r'^courses',views.courses, name='courses'),
        url(r'^list_produits',views.list_produits, name='list_produits'),
        url(r'^edit',views.search_product, name='edit_product'),
        ]


