# Generated by Django 4.2.3 on 2023-08-26 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercice', '0014_vente_prix_unitaire'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vente',
            name='prix_unitaire',
            field=models.PositiveIntegerField(),
        ),
    ]
