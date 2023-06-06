from django.urls import path
from recrutement_api import views 


urlpatterns = [
   path('create/', views.add_demande_recrutement, name='add-demande'),
   path('all/', views.view_demande_recurtement, name='view-demande'),
   path('demande/<int:pk>/delete/', views.delete_demande, name='delete-demande'),
]