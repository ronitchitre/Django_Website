from django.urls import path
from my_app.api.views import api_detail_course_view

app_name = 'my_app'

urlpatterns = [
	path('<slug>/', api_detail_course_view, name = 'detail'),

]