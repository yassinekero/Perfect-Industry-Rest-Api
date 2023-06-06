from django.urls import path
from contact_api import views 



urlpatterns = [
 
   path('create/', views.add_demande_contact, name='add-demande'),
   path('all/', views.view_demande_contact, name='view-demande'),
   path('demande/<int:pk>/delete/', views.delete_demande, name='delete-demande'),
]