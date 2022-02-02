from django.urls import path
from . import views

urlpatterns = [
    path('about/', views.about, name='about'), 
    path('profile/', views.profile_index, name='index'),
    path('jobs/', views.JobList.as_view(), name='job_index'), 
    path('projects/', views.ProjectList.as_view(), name='projects_index'), 
    path('jobs/<int:pk>/', views.JobDetail.as_view(), name='job_detail'), 
    path('jobs/create/', views.JobCreate.as_view(), name='job_create'), 
    path('projects/create', views.ProjectCreate.as_view(), name='project_create'), 
    path('projects/<int:pk>/', views.ProjectDetail.as_view(), name='project_detail'),
    path('projects/<int:project_id>/add_comment/', views.add_comment, name='add_comment'),     
    path('jobs/<int:pk>/update/', views.JobUpdate.as_view(), name='job_update'),
    path('jobs/<int:pk>/delete/', views.JobDelete.as_view(), name='job_delete'), 
    path('projects/<int:pk>/update/', views.ProjectUpdate.as_view(), name='project_update'), 
    path('projects/<int:pk>/delete/', views.ProjectDelete.as_view(), name='project_delete'),
    path('accounts/signup/', views.signup, name='signup'),
    path('memes/add_photo/', views.add_photo, name='add_photo'),
    path('memes/', views.PhotoList.as_view(), name='photo_list'), 
]


