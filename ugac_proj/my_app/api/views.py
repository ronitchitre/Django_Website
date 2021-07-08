from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view 


from my_app.models import Course
from my_app.api.serializers import CourseSerializers


@api_view(['GET'])
def api_detail_course_view(request, slug):
	try:
		course = Course.objects.get(slug = slug)
	except Course.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)
	if request.method == 'GET':
		serializer = CourseSerializers(course)
		return Response(serializer.data)