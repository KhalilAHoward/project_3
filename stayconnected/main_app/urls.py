from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'), #home page path
    path('about/', views.about, name='about'), #page with info about the team and the app
    path('profile/', views.profile_index, name='index'), #<----will add in later
    # path('profile/<int:profile_id>/', views.profile_detail, name='detail'), <---- will add in later
    path('profile/create/', views.ProfileCreate.as_view(), name='profile_create'),
    path('jobs/', views.JobList.as_view(), name='job_index'), #this will be the page that all the job postings show on
    path('projects/', views.ProjectList.as_view(), name='project_index'), #this will be the path for the page that all the projects show on
    path('profile/<int:profile_id>/assoc_project/<int:project_id>/', views.assoc_project, name='assoc_project'), #<----- will add in later
    path('profile/<int:profile_id>/assoc_job/<int:job_id>/', views.assoc_job, name='assoc_job'), #<------- will add in later
    path('jobs/<int:pk>/', views.JobDetail.as_view(), name='job_detail'), #this will be the page when you click the job it shows the details
    path('jobs/create/', views.JobCreate.as_view(), name='job_create'), #this will be the page you can have a form to create a job posting
    path('projects/<int:pk>/', views.ProjectDetail.as_view(), name='project_detail'), #page with details of the project when clicked on
    path('projects/create/', views.ProjectCreate.as_view(), name='project_create'), #page to with a form to create the project
    path('jobs/<int:pk>/update/', views.JobUpdate.as_view(), name='job_update'), #this will be the edit button on the details page of jobs to edit your own job posts
    path('jobs/<int:pk>/delete/', views.JobDelete.as_view(), name='job_delete'), #this will be the delete button on the details page of jobs to delete your job posts
    path('projects/<int:pk>/update/', views.ProjectUpdate.as_view(), name='project_update'), #this will be the edit button on the details page of the project to edit your projects
    path('projects/<int:pk>/delete/', views.ProjectDelete.as_view(), name='project_delete'), #this will be the delete button on details page of the project to delete your own projects

]
# commented out paths are because we dont have a model for it yet.  just creating basic paths for when we include a user profile -Karissa
# charles 

