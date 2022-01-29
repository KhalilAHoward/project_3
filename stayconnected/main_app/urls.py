from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('projects/', views.project_index, name='project_index'),
    path('jobs/', views.job_index, name='job_index'),

]

# charles 

