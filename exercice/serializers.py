from rest_framework import serializers
from .models import *



class ProduitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produit
        fields = "__all__"
        read_only_fields = 'utilisateur',

        #pour ajouter un autre tableau dans le donner qu'on veut
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

     #pour ajouter un autre tableau dans le donner qu'on veut
    def to_representation(self,instance):
        day=super().to_representation(instance)
        #data['exploit']="ken allan"
        day['prix unitaire']=instance.nom.prix_unitaire #nom le foreign key pour appeler ceux du premier tableau
        return day,