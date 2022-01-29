from django.shortcuts import render
from .models import Project, Job
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView



# Add the following import
from django.http import HttpResponse

# Define the home view
def home(request):
  return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1>')

def about(request):
    return render(request, 'home.html')
# changed the below functions to class based views but am not deleting incase we change it back
# def project_index(request):
#     return render(request, 'projects/project_index.html')

# def job_index(request):
#     return render(request, 'jobs/job_index.html')  

# class ProfileCreate(CreateView):
#     model = Profile
#     fields = '__all__' <----profile function for the model we havnt included yet

# def profile_index(request):
#     profiles = Profile.objects.filter(user=request.user)
#     return render(request, 'profile/index.html', {'profiles': profiles}) <--- one more possible profile function

class ProjectList(ListView):
    model = Project

class JobList(ListView):
    model = Job

class JobDetail(DetailView):
    model = Job


class JobCreate(CreateView):
    model = Job
    fields = '__all__'

class ProjectDetail(DetailView):
    model = Project


class ProjectCreate(CreateView):
    model = Project
    fields = '__all__'

class JobUpdate(UpdateView):
    model = Job
    fields = '__all__'


class JobDelete(DeleteView):
    model = Job
    success_url = '/TBD/' # To Be Determined on the success URL

class ProjectUpdate(UpdateView):
    model = Project
    fields = '__all__'


class ProjectDelete(DeleteView):
    model = Project
    success_url = '/TBD/'  # To Be Determined on the success URL


#hi this is working while we are all in different folders

