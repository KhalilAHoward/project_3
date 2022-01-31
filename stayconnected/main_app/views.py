from django.shortcuts import render, redirect
from .models import Project, Job, Profile
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView



# Add the following import
from django.http import HttpResponse

# Define the home view
def home(request):
  return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1>')

def about(request):
    return render(request, 'about.html')
# changed the below functions to class based views but am not deleting incase we change it back
# def project_index(request):
#     return render(request, 'projects/project_index.html')

# def job_index(request):
#     return render(request, 'jobs/job_index.html')  

# def add_project(request, profile_id):
#     form = ProjectForm(request.POST)
#     if form.is_valid():
#         new_project = form.save(commit=false)
#         new_project.profile_id = profile_id
#         new_project.save()
#     return redirect('detail', profile_id=profile_id)

class ProfileCreate(CreateView):
    model = Profile
    fields = '__all__' 

def profile_index(request):
    # profiles = Profile.objects.filter(user=request.user)
    return render(request, 'profile/detail.html') 

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
    success_url = '/profile/' # To Be Determined on the success URL

class ProjectUpdate(UpdateView):
    model = Project
    fields = '__all__'


class ProjectDelete(DeleteView):
    model = Project
    success_url = '/profile/'  # To Be Determined on the success URL

def assoc_project(request, profile_id, project_id):
    profile = Profile.objects.get(id=profile_id)
    profile.projects.add(project_id)
    return redirect('profile', profile_id=profile_id)

def assoc_job(request, profile_id, job_id):
    profile = Profile.objects.get(id=profile_id)
    profile.jobs.add(job_id)
    return redirect('profile', profile_id=profile_id)


#hi this is working while we are all in different folders

