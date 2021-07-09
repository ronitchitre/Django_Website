from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view 
from django.contrib.auth.models import User


from my_app.models import Course
from my_app.api.serializers import CourseSerializer


@api_view(['GET'])
def api_detail_course_view(request, slug):
	try:
		course = Course.objects.get(slug = slug)
	except Course.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)
	if request.method == 'GET':
		serializer = CourseSerializer(course)
		return Response(serializer.data)

@api_view(['PUT'])
def api_update_course_view(request, slug):
	try:
		course = Course.objects.get(slug = slug)
	except Course.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)
	if request.method == 'PUT':
		serializer = CourseSerializer(course, data = request.data)
		data = {}
		if serializer.is_valid():
			serializer.save()
			data['success'] = 'update successful'
			return Response(data = data)
		return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def api_delete_course_view(request, slug):
	try:
		course = Course.objects.get(slug = slug)
	except Course.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)
	if request.method == 'DELETE':
		operation = course.delete()
		data = {}
		if operation:
			data['success'] = 'deleted'
		else:
			data['failed'] =='failed to delete'
		return Response(data = data)

@api_view(['POST'])
def api_create_course_view(request):
	user = User.objects.all().first()
	course = Course(user = user)
	if request.method == 'POST':
		data = {}
		serializer = CourseSerializer(course, data = request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data,status = status.HTTP_201_CREATED)
		return Response(serializer.errors, status =status.HTTP_404_NOT_FOUND)
