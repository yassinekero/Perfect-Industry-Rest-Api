
from django.urls import path
from .views import AuthenticateView, AdminView, DeauthenticateView
urlpatterns = [

     path("authenticate", AuthenticateView.as_view()),
     path("admin", AdminView.as_view()),
     path("deauthenticate",  DeauthenticateView.as_view())
]
