from django.shortcuts import redirect
from .models import *
from django.db.models import Q

def search(request):
   try:
    # get the search term from the search bar where the name of the input field is search.
    searchRequest = request.POST.get('search') 
    
    # the query that allows us to search more than one field in one query. 
    searchable = Q(jobTitle__icontains= searchRequest) | Q(jobDescription__icontains= searchRequest)  
   
    # get all the results containting the search term.
    result = JobDetails.objects.filter(searchable)
          
    # send the result to a template called search.html to process the result their. 
    return render(request, 'app/search.html', {"result":result}) 
    
   
   except:
    return redirect("index") # get back to the homepage if an error occurs. 
