from django.shortcuts import render
from .models import Product
from .forms import ProductFilterForm

def product_list(request):
    products = Product.objects.all()
    form = ProductFilterForm(request.GET)

    if form.is_valid():
        if form.cleaned_data.get('min_price'):
            products = products.filter(price__gte=form.cleaned_data['min_price'])
        if form.cleaned_data.get('max_price'):
            products = products.filter(price__lte=form.cleaned_data['max_price'])
        if form.cleaned_data.get('brand'):
            products = products.filter(brand__icontains=form.cleaned_data['brand'])
        if form.cleaned_data.get('min_rating'):
            products = products.filter(rating__gte=form.cleaned_data['min_rating'])
        if form.cleaned_data.get('category'):
            products = products.filter(category__icontains=form.cleaned_data['category'])

    return render(request, 'products/product_list.html', {'products': products, 'form': form})

# Price range example: "https://www.amazon.com/s?k=dog+food&low-price=XX&high-price=XX"