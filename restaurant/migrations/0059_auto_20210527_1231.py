# Generated by Django 3.1.6 on 2021-05-27 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0058_auto_20210527_1048'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='supplement',
            name='sup_frite',
        ),
        migrations.AddField(
            model_name='supplement',
            name='sup_salee',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name='supplement',
            name='sup_sucree',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name='supplement',
            name='sup_sur_frite',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
