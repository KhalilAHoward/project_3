
# Jake was here (branch name John)

from django.db import models
from datetime import date
from django.contrib.auth.models import User
# Create your models here.


class Project(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=250)
    link = models.CharField(max_length=200)


class Job(models.Model):
    company_name = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    link = models.CharField(max_length=200)
    salary_min = models.IntegerField()
    salary_max = models.IntegerField()
    date = models.DateField('Date Posted')

    class Meta:
        ordering = ['-date']

    # def __str__(self):

    #     return f"{self.get_link_display()} on {self.date}"

class Profile(models.Model):
    name = models.CharField(max_length=50)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
