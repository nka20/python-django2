from rest_framework import viewsets,mixins
from rest_framework.permissions import *
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.authentication import SessionAuthentication
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import *
from .serializers import *

class TokenPairView(TokenObtainPairView):
        serializer_class=TokenPairSerializer

class ProduitViewset(viewsets.ModelViewSet):
    queryset= Produit.objects.all() 
    permission_classes= IsAuthenticatedOrReadOnly,
    authentication_classes= JWTAuthentication, SessionAuthentication
    serializer_class=ProduitSerializer

    def perform_create(self,serializer):
        serializer.save(utilisateur=self.request.user)
        return serializer

    @action(methods=['POST'],
        detail=False,
        url_name=r"search",
        url_path=r"search",
        permission_classes=[IsAuthenticated],
        serializer_class=SearchSerializer
         )
    def search(self,request):
        data=request.data
        produits=Produit.objects.filter(nom__icontains=data['keyword'])
        serializer=ProduitSerializer(produits,many=True)
        return Response(serializer.data,200)
        
class VenteViewset(viewsets.ModelViewSet):
    queryset= Vente.objects.all()
    permission_classes= IsAuthenticatedOrReadOnly,
    authentication_classes= JWTAuthentication, SessionAuthentication
    serializer_class=VenteSerializer


    def perform_create(self, serializer):
        data=serializer.validated_data
        quantite=data['quantite']
        produit=data['nom']
        prix=produit.prix_unitaire
        serializer.save(nom=data['nom'],prix_unique=prix,prix_total=quantite * prix,utilisateur=self.request.user )
        return serializer

        @action(methods=['POST'],
        detail=False,
        url_name=r"search",
        url_path=r"search",
        permission_classes=[IsAuthenticated],
        serializer_class=SearchSerializer
         )
        def search(self,request):
            data=request.data
            ventes=Vente.objects.filter(nom__icontains=data['keyword'])
            serializer=VenteSerializer(ventes,many=True)
            return Response(serializer.data,200)

