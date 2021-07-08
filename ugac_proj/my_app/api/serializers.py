from rest_framework import serializers
from my_app.models import Course

class CourseSerializers(serializers.ModelSerializer):
	class Meta:
		model = Course
		fields = ['name', 'description', 'date_posted', 'prereq', 'dep']