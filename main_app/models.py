from django.urls import reverse
from django.db import models
from datetime import date
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Project(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=250)
    link = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

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

class Profile(models.Model):
    username = models.CharField(max_length=50)
    user = models.OneToOneField(
        User, 
        on_delete=models.CASCADE,
        primary_key=True,
        )

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def update_profile_signal(sender, instance, created, **kwargs):
    print(sender, instance, created)
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()

def get_absolute_url(self):
    return reverse('detail', kwargs={'profile_id': self.pk})
        


class Comment(models.Model):
    comment = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ['created_on']

class Photo(models.Model):
    url = models.CharField(max_length=200)


    def __str__(self):
        return f"Photo for: @{self.url}"

class ProfilePhoto(models.Model):
    url = models.CharField(max_length=200, blank=True, null=True)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    

    def __str__(self):
        return f"Photo for profile_id: {self.profile_id} {self.url}"


