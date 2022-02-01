from django.shortcuts import render, redirect
from .models import Project, Job, Profile
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse


def home(request):
    return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1>')


def about(request):
    return render(request, 'about.html')

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

        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)

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
    success_url = '/profile/'  


class ProjectUpdate(UpdateView):
    model = Project
    fields = '__all__'


class ProjectDelete(DeleteView):
    model = Project
    success_url = '/profile/'  


