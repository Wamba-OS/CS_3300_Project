from django.shortcuts import render
from .models import Product, BlockedDomain
from .forms import ProductFilterForm

def product_list(request):
    products = Product.objects.all()
    form = ProductFilterForm(request.GET)

    # Handle blocked domains input from form (if provided)
    blocked_domains_input = request.GET.get('blocked_domains', '')
    if blocked_domains_input:
        blocked_domains_list = [domain.strip() for domain in blocked_domains_input.split(',')]
        blocked_domains = BlockedDomain.objects.filter(domain__in=blocked_domains_list)
        # Exclude products from blocked domains
        products = products.exclude(domain__in=blocked_domains_list)

    # Existing filtering logic (price, brand, rating, etc.)
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
