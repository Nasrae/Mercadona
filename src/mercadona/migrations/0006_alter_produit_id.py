# Generated by Django 4.2.1 on 2023-05-10 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mercadona', '0005_alter_produit_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produit',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
