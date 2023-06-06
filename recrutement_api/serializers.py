from rest_framework import serializers 
from recrutement_api.models import Demande
 

class DemandeSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Demande
        fields = (
            'id',
                  'prenom',
                  'nom',
                  'email',
                  'telephone',
                  'occupation',
                  'lienCv')