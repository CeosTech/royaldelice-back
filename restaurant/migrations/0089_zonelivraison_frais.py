# Generated by Django 3.1.6 on 2021-12-24 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0088_ingredient_disponibilite'),
    ]

    operations = [
        migrations.AddField(
            model_name='zonelivraison',
            name='frais',
            field=models.FloatField(blank=True, default=0),
        ),
    ]
