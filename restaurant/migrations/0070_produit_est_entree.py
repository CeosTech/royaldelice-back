# Generated by Django 3.1.6 on 2021-11-26 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0069_auto_20210901_0835'),
    ]

    operations = [
        migrations.AddField(
            model_name='produit',
            name='est_entree',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
