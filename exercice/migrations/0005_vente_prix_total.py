# Generated by Django 4.2.3 on 2023-07-28 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercice', '0004_remove_vente_prix_total'),
    ]

    operations = [
        migrations.AddField(
            model_name='vente',
            name='prix_total',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
    ]
