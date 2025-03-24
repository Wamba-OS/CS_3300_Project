# Imports
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .forms import SearchForm
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
        if form.is_valid:
            query = form.cleaned_data['query']

            # Format the search
            formatted_search = urllib.parse.quote_plus(query)

            # Format the URL
            formatted_url = f"https://www.amazon.com/s?k={formatted_search}"

            # Display the results
            return render(request, 'search_app/results.html', {
                'query': query,
                'amazon_url': formatted_url
            })

    # Redirect user to Amazon page with their input
    return redirect('get_search')

