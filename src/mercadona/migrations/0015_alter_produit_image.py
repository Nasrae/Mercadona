# Generated by Django 4.2.1 on 2023-05-11 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mercadona', '0014_rename_descritpion_produit_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produit',
            name='image',
            field=models.ImageField(upload_to='mercadona/static/mercadona/images'),
        ),
    ]