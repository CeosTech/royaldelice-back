# Generated by Django 3.1.6 on 2021-12-20 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0075_auto_20211220_1238'),
    ]

    operations = [
        migrations.CreateModel(
            name='TypeSupplement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100, unique=True)),
            ],
        ),
    ]