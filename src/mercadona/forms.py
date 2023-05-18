from django import forms
from .models import produit, promotion, categorie


class produitForm(forms.ModelForm):
    class Meta:
        model = produit
        fields = ('label', 'description', 'prix', 'image')

class promotionForm(forms.ModelForm):
    class Meta:
        model = promotion
        fields = ('promo_ID', 'promotion', 'durer')

class categorieForm(forms.ModelForm):
    class Meta:
        model = categorie
        fields = ('label',)