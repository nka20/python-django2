# Generated by Django 4.2.3 on 2023-07-28 20:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exercice', '0003_rename_user_produit_utilisateur_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vente',
            name='prix_total',
        ),
    ]