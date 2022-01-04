from rest_framework import serializers
from main.models import Student_on_lesson


class Student_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Student_on_lesson
        fields = ['date', 'student']
