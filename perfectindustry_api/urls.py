
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/recrutement/', include('recrutement_api.urls')),
    path('api/contact/', include('contact_api.urls')),
    path('api/suivi/', include('suivi.urls')),
    path('api/admin/', include('adminAccount.urls')),
]
