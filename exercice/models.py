from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Produit(models.Model):
    id=models.AutoField(primary_key=True)
    nom=models.CharField(max_length=50)
    prix_unitaire=models.IntegerField()
    utilisateur=models.ForeignKey(User,on_delete=models.PROTECT)

    def __str__(self):
       return f" {self.nom}"

class Vente(models.Model):
    id=models.AutoField(primary_key=True)
    nom=models.ForeignKey(Produit,on_delete=models.CASCADE)# pour garder les donnee meme si on laisse un null sur ionic meme si on supprime le foreign key relier
    quantite= models.PositiveIntegerField()
    prix_total=models.FloatField()
    prix_unique=models.PositiveIntegerField()
    utilisateur=models.ForeignKey(User,on_delete=models.PROTECT)

