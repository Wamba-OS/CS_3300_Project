from django import forms
from .models import Product

class ProductFilterForm(forms.Form):
    min_price = forms.DecimalField(required=False, max_digits=10, decimal_places=2, label="Min Price")
    max_price = forms.DecimalField(required=False, max_digits=10, decimal_places=2, label="Max Price")
    brand = forms.CharField(required=False, label="Brand")
    min_rating = forms.FloatField(required=False, label="Min Rating")
    category = forms.CharField(required=False, label="Category")
