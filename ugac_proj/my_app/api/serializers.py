from rest_framework import serializers
from my_app.models import Course

class CourseSerializer(serializers.ModelSerializer):
	class Meta:
		model = Course
		fields = ['name', 'description', 'prereq', 'dep', 'available', 'slug']