
# Jake was here (branch name John)
from django.forms import DateInput, DateTimeInput
from django.urls import reverse
from django.db import models
from datetime import date
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=250)
    link = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('project_detail', kwargs={'pk': self.id})

class Job(models.Model):
    company_name = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    link = models.CharField(max_length=200)
    salary_min = models.IntegerField()
    salary_max = models.IntegerField()
    date = models.DateField('Date Posted')

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('job_detail', kwargs={'pk': self.id})

    # def __str__(self):

    #     return f"{self.get_link_display()} on {self.date}"

class Profile(models.Model):
    username = models.CharField(max_length=50)
    user = models.OneToOneField(
        User, 
        on_delete=models.CASCADE,
        primary_key=True,
        )

#     def __str__(self):
#         return self.user.username

# @receiver(post_save, sender=User)
# def update_profile_signal(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)
#     instance.profile.save()


    def __str__(self):
        return f'{self.user.username} Profile'

# class Profile(models.Model):
#     name = models.CharField(max_length=50)
#     project = models.ForeignKey(Project, on_delete=models.CASCADE)
#     job = models.ForeignKey(Job, on_delete=models.CASCADE)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.name

    def get_absolute_url(self):
        print(self, 'this is selffff')
        return reverse('detail', kwargs={'profile_id': self.pk})
        


class Comment(models.Model):
    comment = models.TextField()
    created_on = models.DateTimeField(default=DateTimeInput)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

