from django import forms

class SearchForm(forms.Form):
    query = forms.CharField(max_length=50, label='Search Amazon for:')


class ProductFilterForm(forms.Form):
    min_price = forms.DecimalField(required=False, max_digits=10, decimal_places=2, label="Min Price")
    max_price = forms.DecimalField(required=False, max_digits=10, decimal_places=2, label="Max Price")
    brand = forms.CharField(required=False, label="Brand")
    min_rating = forms.FloatField(required=False, label="Min Rating")
    category = forms.CharField(required=False, label="Category")


