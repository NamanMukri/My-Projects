from django.db import models

class Patient(models.Model):  
  patient_regNo=models.TextField(unique=True,max_length=20)
  patient_name= models.TextField(max_length=20)
  patient_email=models.TextField(max_length=20)
  patient_mobile=models.TextField(max_length=10)
  admitted_at=models.DateTimeField(auto_now_add=True)
  def __str__(self):
    return self.patient_name