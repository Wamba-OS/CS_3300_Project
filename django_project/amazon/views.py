# Imports
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .forms import SearchForm, ProductFilterForm
import urllib.parse


# Load the welcome form
def welcome(request):
    return render(request, 'search_app/welcome.html')

def get_search(request):
    form = SearchForm
    return render(request, 'search_app/get_search.html', {'form': form})

# Get the user's search
def results(request):

    # Validate Search
    if request.method == 'POST':
        form = SearchForm(request.POST)

        # Validate form
        if form.is_valid():
            query = form.cleaned_data['query']

            # Format the search
            formatted_search = urllib.parse.quote_plus(query)

            ## Error checking
            # If is not alphanumeric, then return an error
            if not formatted_search.isalnum:
                return redirect('no_search')

            # Format the URL
            formatted_url = f"https://www.amazon.com/s?k={formatted_search}"

            # Display the results
            return render(request, 'search_app/results.html', {
                'query': query,
                'amazon_url': formatted_url
            })

    # Redirect user to Amazon page with their input
    return redirect('get_search')

# Filtering View
def product_list(request):
    # products = Product.objects.all()
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
