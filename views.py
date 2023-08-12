from django.shortcuts import redirect
from .models import *
from django.db.models import Q

def search(request):
   try:
    searchRequest = request.POST.get('search') # get the search term from the search bar where the name of the input field is search.
    
    #search in the job title and the job description fields of the table if they contain the search term. 
    searchable = Q(jobTitle__icontains= searchRequest) | Q(jobDescription__icontains= searchRequest)  

    result = JobDetails.objects.filter(searchable) # get all the results containting the search term.
    
     return render(request, 'app/search.html', {"result":result}) # send the result to a template called search.html to process the result their. 
   
  except:
       return redirect("index") # get back to the homepage if an error occurs. 
