from rest_framework import serializers
from .models import *



class ProduitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produit
        fields = "__all__"
        read_only_fields = 'utilisateur',
class VenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vente
        fields = "__all__"
        read_only_fields = 'prix_total',