from rest_framework import serializers 
from contact_api.models import Demande
 

class DemandeSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Demande
        fields = (
            'id',
                  'prenom',
                  'nom',
                  'email',
                  'telephone',
                  'message'
                  )