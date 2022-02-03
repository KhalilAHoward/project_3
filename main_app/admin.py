from django.contrib import admin

from .models import Project, Job, Profile, Photo, ProfilePhoto
# Register your models here
admin.site.register(Project)
admin.site.register(Job)
admin.site.register(Profile)
admin.site.register(Photo)
admin.site.register(ProfilePhoto)
