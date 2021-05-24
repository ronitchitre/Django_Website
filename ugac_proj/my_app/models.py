from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.urls import reverse

class Course(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    prereq = models.CharField(max_length=50)
    dep = models.CharField(max_length=50)
    available = models.BooleanField()

    def __str__(self):
        return self.name

class CourseSelected(models.Model):
    name = models.CharField(max_length=50)
    student = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('app-home')