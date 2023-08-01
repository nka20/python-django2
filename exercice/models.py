from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Produit(models.Model):
    id=models.AutoField(primary_key=True)
    nom=models.CharField(max_length=50)
    prix_unitaire=models.IntegerField(unique=True)
    utilisateur=models.ForeignKey(User,on_delete=models.PROTECT)


    def __str__(self):
       return f" {self.nom}"

class Vente(models.Model):
    id=models.AutoField(primary_key=True)
    nom=models.ForeignKey(Produit,on_delete=models.PROTECT)
    quantite= models.PositiveIntegerField()
    prix_total=models.FloatField()
    utilisateur=models.ForeignKey(User,on_delete=models.PROTECT)

