# Generated by Django 4.2.3 on 2023-08-26 19:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exercice', '0012_alter_vente_nom'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vente',
            name='nom',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='exercice.produit'),
        ),
    ]
