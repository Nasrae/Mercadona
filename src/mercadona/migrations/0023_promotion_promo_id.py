# Generated by Django 4.2.1 on 2023-05-18 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mercadona', '0022_remove_promotion_promo_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='promotion',
            name='promo_ID',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
