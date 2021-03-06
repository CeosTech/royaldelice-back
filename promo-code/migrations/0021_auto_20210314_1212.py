# Generated by Django 3.1.6 on 2021-03-14 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0020_auto_20210314_1159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produit',
            name='image',
            field=models.ImageField(null=True, upload_to='./static/images'),
        ),
        migrations.AlterField(
            model_name='produit',
            name='nom',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
