from rest_framework import serializers
from .models import *



class ProduitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produit
        fields = "__all__"
        read_only_fields = 'utilisateur',
    def to_representation(self,instance):
        data=super().to_representation(instance)
        #data['exploit']="ken allan"
        data['ineza']=instance.nom
        return data,
class VenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vente
        fields = "__all__"
        read_only_fields = 'prix_total','utilisateur',