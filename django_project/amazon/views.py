# Imports
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .forms import SearchForm
import urllib.parse


# Load the welcome form
def welcome(request):
    return render(request, 'welcome.html')

def display_search(request):
    form = SearchForm
    return render(request, 'amazon/get_search.html', {'form': form})

# Get the user's search
def user_search(request):

    # Validate Search
    if request.method == 'POST':
        form = SearchForm(request.POST)

        # Validate form
        if form.is_valid:
            query = form.cleaned_data['query']

            # Format the search
            formatted_search = urllib.parse.quote_plus(query)

            # Format the URL
            formatted_url = f"https://www.amazon.com/s?k={formatted_search}"
            return render(request, 'search')

    # Redirect user to Amazon page with their input
    return redirect(formatted_url)

