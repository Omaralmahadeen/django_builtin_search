# Import necessary modules
from django.shortcuts import redirect
from .models import *
from django.db.models import Q

# Define the search function
def search(request):
    try:
        # Get the search query from the POST request
        searchRequest = request.POST.get('search')
        
        # Define the conditions for searching in jobTitle and jobDescription using Q objects
        searchable = Q(jobTitle__icontains=searchRequest) | Q(jobDescription__icontains=searchRequest)
        
        # Perform the search using the defined conditions
        result = JobDetails.objects.filter(searchable)
        
        # Render the search results using the 'search.html' template and pass the results as context
        return render(request, 'app/search.html', {"result": result})
        
    except:
        # If an exception occurs redirect to the "index" (home page) 
        return redirect("index")
