from rest_framework import serializers
from student import models

class StudentSerializer(serializers.ModelSerializer):
  class Meta:
    model=models.Student
    fields='__all__'