from . import views
from .views import CourseSelectedView, CourseCreateView, CourseUpdateView, CourseDeleteView
from django.urls import path

urlpatterns = [
    path('', views.CourseSelectedView.as_view(), name='app-home'),
    path('about/', views.about, name='app-about'),
    path('course/new/', CourseCreateView.as_view(), name = 'course-create'),
    path('course/<int:pk>/update/', CourseUpdateView.as_view(), name = 'course-update'),
    path('course/<int:pk>/delete/', CourseDeleteView.as_view(), name = 'course-delete')
]