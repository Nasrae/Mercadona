# Generated by Django 4.2.1 on 2023-05-10 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mercadona', '0009_alter_produit_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produit',
            name='image',
            field=models.ImageField(upload_to='.static/mercadona/images/'),
        ),
    ]
