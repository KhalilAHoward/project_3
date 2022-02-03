from django.shortcuts import render, redirect
from .models import Project, Job, Profile, Photo, ProfilePhoto
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
import uuid
import boto3
from .forms import CommentForm
import botocore
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
import os

S3_BASE_URL = 'https://s3-us-west-1.amazonaws.com/'
BUCKET = 'sei-stay-connected'
my_key = os.environ['AWS_SECRET_ACCESS_KEY']

def home(request):
    return HttpResponseRedirect('/about/')


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
            return redirect('index')

        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)


@login_required
def profile_index(request):
    profile = Profile.objects.get(user=request.user)
    projects = Project.objects.filter(user=request.user)
    profile_pic = profile.profilephoto_set.all()
    return render(request, 'profile/detail.html', {'profile': profile, 'projects': projects, 'profile_pic':profile_pic[0]})


def add_comment(request, project_id):

    form = CommentForm(request.POST)

    if form.is_valid():
        new_comment = form.save(commit=False)
        new_comment.project_id = project_id
        new_comment.save()
    return redirect('project_detail', project_id)


class ProjectList(LoginRequiredMixin, ListView):
    model = Project
    template = 'job_list.html'


class JobList(ListView):
    model = Job


class JobDetail(DetailView):
    model = Job


class JobCreate(LoginRequiredMixin, CreateView):
    model = Job
    fields = '__all__'


class ProjectDetail(LoginRequiredMixin, DetailView):
    model = Project

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        return context


class ProjectCreate(LoginRequiredMixin, CreateView):
    model = Project
    fields = '__all__'


class JobUpdate(LoginRequiredMixin, UpdateView):
    model = Job
    fields = '__all__'


class JobDelete(LoginRequiredMixin, DeleteView):
    model = Job
    success_url = '/profile/'


class ProjectUpdate(LoginRequiredMixin, UpdateView):
    model = Project
    fields = '__all__'


class ProjectDelete(LoginRequiredMixin, DeleteView):
    model = Project
    success_url = '/profile/'


def add_photo(request):
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')

        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        key = uuid.uuid4().hex[:6] + \
            photo_file.name[photo_file.name.rfind('.'):]

        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            url = f"{S3_BASE_URL}{BUCKET}/{key}"
            photo = Photo(url=url)
            photo.save()
        except botocore.exceptions.ClientError as error:
            print(error, " <-this aws error")
    return redirect('photo_list')


class PhotoList(ListView):
    model = Photo
    template = 'photo_list.html'

def add_profile_photo(request, profile_id):
    photo_file = request.FILES.get('photo-file', None)

    if photo_file:
        s3 = boto3.client('s3')
        key = uuid.uuid4().hex[:6] + \
            photo_file.name[photo_file.name.rfind('.'):]

        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            url = f"{S3_BASE_URL}{BUCKET}/{key}"
            ProfilePhoto.objects.update_or_create(url=url, profile_id=profile_id)

        except:
            print('An error occurred uploading file to s3, is your access key correct?')
    return redirect('index')



