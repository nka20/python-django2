# Generated by Django 4.2.3 on 2023-07-28 20:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exercice', '0007_vente_utilisateur'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vente',
            name='utilisateur',
        ),
    ]
