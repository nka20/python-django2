# Generated by Django 4.2.3 on 2023-08-08 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercice', '0009_vente_utilisateur'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produit',
            name='prix_unitaire',
            field=models.IntegerField(),
        ),
    ]
