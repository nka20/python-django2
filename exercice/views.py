from rest_framework import viewsets,mixins
from rest_framework.permissions import *

from .models import *
from .serializers import *

class ProduitViewset(viewsets.ModelViewSet):
    queryset= Produit.objects.all() 
    permission_classes= IsAuthenticatedOrReadOnly,
    serializer_class=ProduitSerializer

    def perform_create(self,serializer):
        serializer.save(utilisateur=self.request.user)
        return serializer

class VenteViewset(viewsets.ModelViewSet):
    queryset= Vente.objects.all()
    permission_classes= IsAuthenticatedOrReadOnly,
    serializer_class=VenteSerializer


    def perform_create(self, serializer):
        data=serializer.validated_data
        quantite=data['quantite']
        produit=data['nom']
        prix=produit.prix_unitaire
        serializer.save(prix_total=quantite * prix )
        return serializer
