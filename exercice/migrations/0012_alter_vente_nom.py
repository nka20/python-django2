# Generated by Django 4.2.3 on 2023-08-26 19:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exercice', '0011_alter_vente_nom'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vente',
            name='nom',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='exercice.produit'),
            preserve_default=False,
        ),
    ]