from django.shortcuts import render, redirect
from .models import Project, Job, Profile, Photo
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
import uuid
import boto3

# Add the following import
from django.http import HttpResponse

S3_BASE_URL = 'https://s3-us-west-1.amazonaws.com/'
BUCKET = 'sei-stay-connected'

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


def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            print(user, 'this is the user')
            print(dir(user))
            login(request, user)

            profile = Profile(user=user, username=user.username)
            print(profile)
            profile.save()
            return redirect('index')

            # return redirect('profile_form')

        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)

# class ProfileCreate(CreateView):
#     model = Profile
#     fields = ['user']

#     def form_valid(self, form):
#         self.object = form.save()
#         return super().form_valid(form)
#         form.instance.user = self.request.user
#         return super().form_valid(form)


def profile_index(request):
    profile = Profile.objects.get(user=request.user)
    return render(request, 'profile/detail.html', {'profile':profile}) 
    

class ProjectList(ListView):
    model = Project
    template = 'job_list.html'


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
    success_url = '/profile/'  # To Be Determined on the success URL


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


# hi this is working while we are all in different folders

def add_photo(request, user_id):
    # photo-file will be the "name" attribute on the <input type="file">
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        # need a unique "key" for S3 / needs image file extension too
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        # just in case something goes wrong
        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            # build the full url string
            url = f"{S3_BASE_URL}{BUCKET}/{key}"
            # we can assign to cat_id or cat (if you have a cat object)
            Photo.objects.create(url=url, user_id=user_id)
        except:
            print('An error occurred uploading file to S3')
    return redirect('detail', user_id=user_id)