from django.contrib import admin
from .models import produit, promotion, categorie

# Register your models here.

admin.site.register(produit)
admin.site.register(promotion)
admin.site.register(categorie)
