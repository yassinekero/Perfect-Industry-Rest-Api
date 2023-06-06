from rest_framework import serializers 
from suivi.models import Produit
 

class ProduitSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Produit
        fields = (
            'id',
                  'produit_nom',
                  'client',
                  'status',
                  )