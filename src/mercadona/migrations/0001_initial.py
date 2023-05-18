# Generated by Django 4.2.1 on 2023-05-10 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='produit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=50)),
                ('descritpion', models.CharField(max_length=200)),
                ('prix', models.FloatField()),
                ('image', models.ImageField(upload_to='', width_field=450)),
                ('categorie', models.CharField(max_length=20)),
            ],
        ),
    ]