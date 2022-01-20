from rest_framework import serializers
from patient import models

class PatientSerializer(serializers.ModelSerializer):
  class Meta:
    model=models.Patient
    fields='__all__'