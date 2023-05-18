from django.db import models

class produit(models.Model):
    id = models.AutoField(primary_key=True)
    label = models.CharField(max_length=50)
    description = models.TextField(max_length=250)
    prix = models.DecimalField(max_digits=15, decimal_places=2)
    image = models.ImageField(upload_to='mercadona/static/mercadona/images')

class promotion(models.Model):
    id = models.AutoField(primary_key=True)
    promotion = models.IntegerField(blank=True, null=True)
    durer = models.DurationField(null=True)

class categorie(models.Model):
    id = models.AutoField(primary_key=True)
    label = models.CharField(max_length=20)