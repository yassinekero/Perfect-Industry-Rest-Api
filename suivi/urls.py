from django.urls import path
from . import views



urlpatterns = [
 
   path('create/', views.add_produit, name='add-produit'),
   path('all/', views.view_produit, name='view-produit'),
   path('produit/<int:pk>/update', views.update_produit, name='update-produit'),
   path('produit/<int:pk>/delete/', views.delete_produit, name='delete-produit'),
]