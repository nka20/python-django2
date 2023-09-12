from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import *

class TokenPairSerializer(TokenObtainPairSerializer):
    def validate(self,attrs):
        data=super(TokenPairSerializer,self).validate(attrs)

        data['groups']=[group.name for group in self.user.groups.all()]
        data['username']=self.user.username
        data['id']=self.user.id
        data['first_name']=self.user.first_name
        data['last_name']=self.user.last_name
        data['is_superuser']=self.user.is_superuser
        return data

class ProduitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produit
        fields = "__all__"
        read_only_fields = 'utilisateur',

        #pour ajouter un autre tableau dans le donner qu'on veut
    def to_representation(self,instance):
        data=super().to_representation(instance)
        data['exploit']="ken allan"
        data['ineza']=instance.nom
        return data 

class SearchSerializer(serializers.Serializer):
    keyword=serializers.CharField(required=True)
    
class VenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vente
        fields = "__all__"
        read_only_fields = 'utilisateur',

class SearchSerializer(serializers.Serializer):
    keyword=serializers.CharField(required=True)
