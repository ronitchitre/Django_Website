from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.urls import reverse

class Course(models.Model):
    name = models.CharField(max_length=50, blank = True)
    description = models.TextField(blank = True)
    date_posted = models.DateTimeField(default=timezone.now, blank = True)
    prereq = models.CharField(max_length=50, blank = True)
    dep = models.CharField(max_length=50, blank = True)
    available = models.BooleanField(blank = True, default = True)
    def_user = User.objects.all().first()
    user = models.ForeignKey(User, on_delete=models.CASCADE, default = def_user)
    slug = models.SlugField(max_length = 250,  blank = True)

    def __str__(self):
        return self.name

class CourseSelected(models.Model):
    name = models.CharField(max_length=50)
    student = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('app-home')