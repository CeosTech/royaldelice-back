# Generated by Django 3.1.6 on 2021-11-26 11:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0071_auto_20211126_1227'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='produit',
            name='taille_pizza',
        ),
    ]
