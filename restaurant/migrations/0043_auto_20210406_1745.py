# Generated by Django 3.1.6 on 2021-04-06 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0042_auto_20210402_1237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produit',
            name='prix_supplement',
            field=models.FloatField(default=1.5),
        ),
    ]
