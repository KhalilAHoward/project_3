from django.shortcuts import render
from .models import Project, Job

# Add the following import
from django.http import HttpResponse

# Define the home view
def home(request):
  return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1>')

def about(request):
    return render(request, 'home.html')

def project_index(request):
    return render(request, 'projects/project_index.html')

def job_index(request):
    return render(request, 'jobs/job_index.html')


#hi this is working while we are all in different folders

