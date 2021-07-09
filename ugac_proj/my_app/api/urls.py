from django.urls import path
from my_app.api.views import *

app_name = 'my_app'

urlpatterns = [
	path('<slug>/', api_detail_course_view, name = 'detail'),
	path('<slug>/update/', api_update_course_view, name = 'update'),
	path('<slug>/delete/', api_delete_course_view, name = 'delete'),
	path('create', api_create_course_view, name = 'create'),

]