from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader

#def start_main(request):
    # Load the first template
    #template = loader.get_template('main.html')
    #return HttpResponse(template.render())

def produce_query(request):

    # Get the user's raw search
    initial_search = request.GET.get("query", "")

    # Check to see if a search was entered
    if not initial_search:
      
        # If search was not entered, go to error page and ask again
        #return render(request, "no_search.html", {"error" : "Please enter a new search"})
        return render(request, "main.html", {"error" : "Please enter a new search"})

    # Format the search
    formatted_search = initial_search.replace(' ', '+')

    # Format the URL
    formatted_url = f"https://www.amazon.com/s?k={formatted_search}"

    # Redirect user to Amazon page with their input
    return redirect(formatted_url)

