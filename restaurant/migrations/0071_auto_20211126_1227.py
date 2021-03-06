# Generated by Django 3.1.6 on 2021-11-26 11:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0070_produit_est_entree'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='produit',
            name='est_assiette',
        ),
        migrations.RemoveField(
            model_name='produit',
            name='est_crepe_salee',
        ),
        migrations.RemoveField(
            model_name='produit',
            name='est_crepe_sucree',
        ),
        migrations.RemoveField(
            model_name='produit',
            name='est_croque',
        ),
        migrations.RemoveField(
            model_name='produit',
            name='est_menu_burgers',
        ),
        migrations.RemoveField(
            model_name='produit',
            name='est_menu_crepe_salee',
        ),
        migrations.RemoveField(
            model_name='produit',
            name='est_menu_croque',
        ),
        migrations.RemoveField(
            model_name='produit',
            name='est_menu_enfant',
        ),
        migrations.RemoveField(
            model_name='produit',
            name='est_menu_family',
        ),
        migrations.RemoveField(
            model_name='produit',
            name='est_menu_paninis',
        ),
        migrations.RemoveField(
            model_name='produit',
            name='est_menu_sandwichs',
        ),
        migrations.RemoveField(
            model_name='produit',
            name='est_menu_sandwichs_au_four',
        ),
        migrations.RemoveField(
            model_name='produit',
            name='est_menu_tacos',
        ),
        migrations.RemoveField(
            model_name='produit',
            name='est_milkshake',
        ),
        migrations.RemoveField(
            model_name='produit',
            name='est_panini',
        ),
        migrations.RemoveField(
            model_name='produit',
            name='est_pizza_creme_fraiche',
        ),
        migrations.RemoveField(
            model_name='produit',
            name='est_pizza_sauce_barbecue',
        ),
        migrations.RemoveField(
            model_name='produit',
            name='est_pizza_sauce_tomate',
        ),
        migrations.RemoveField(
            model_name='produit',
            name='est_salade_pate',
        ),
        migrations.RemoveField(
            model_name='produit',
            name='est_smoothie',
        ),
    ]
