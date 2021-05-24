from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
# from django.views.generic.detail import t
from .models import Course, CourseSelected
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import UserPassesTestMixin
from django.utils.decorators import method_decorator

# Create your views here.

@login_required
def home(request):
    context = {
        'info': Course.objects.all(),
        'course': CourseSelected.objects.all()
    }
    return render(request, 'my_app/home.html', context)

@login_required
def about(request):
    return render(request, 'my_app/about.html', {'title': 'About Section', 'info':Course.objects.all()})

@method_decorator(login_required, name='dispatch')
class CourseSelectedView(ListView):
    model = CourseSelected
    template_name = 'my_app/home.html'
    context_object_name = 'course'

@method_decorator(login_required, name='dispatch')
class CourseCreateView(CreateView):
    model = CourseSelected
    fields = ['name']
    template_name = 'my_app/course_form.html'

    def form_valid(self, form):
        form.instance.student = self.request.user
        return super().form_valid(form)
    
@method_decorator(login_required, name='dispatch')
class CourseUpdateView(UserPassesTestMixin,UpdateView):
    model = CourseSelected
    fields = ['name']
    template_name = 'my_app/course_form.html'
    def form_valid(self, form):
        form.instance.student = self.request.user
        return super().form_valid(form)
    def test_func(self):
        course = self.get_object()
        if self.request.user == course.student:
            return True
        else:
            return False

@method_decorator(login_required, name='dispatch')
class CourseDeleteView(UserPassesTestMixin,DeleteView):
    model = CourseSelected
    template_name = 'my_app/delete.html'
    success_url = '/'
    def test_func(self):
        course = self.get_object()
        if self.request.user == course.student:
            return True
        else:
            return False
