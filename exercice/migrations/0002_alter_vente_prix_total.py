# Generated by Django 4.2.3 on 2023-07-28 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercice', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vente',
            name='prix_total',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
    ]