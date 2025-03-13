from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def produce_query(request):

    # Get the user's raw search
    initial_search = request.GET.get("query", "")

    # Check to see if a search was entered
    if initial_search:

        # Format the search
        formatted_search = initial_search.replace(' ', '+')

        # Format the URL
        formatted_url = f"https://www.amazon.com/s?k={formatted_search}"

        # Redirect user to Amazon page with their input
        return redirect(formatted_url)
        


    
    return render(request, "no_search.html")