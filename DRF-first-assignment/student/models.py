from django.db import models


class Student(models.Model):  
  student_regNo=models.TextField(unique=True,max_length=20)
  student_name= models.TextField(max_length=20)
  student_email=models.TextField(max_length=20)
  student_mobile=models.TextField(max_length=10)
  created_at=models.DateTimeField(auto_now_add=True)
  def __str__(self):
    return self.student_name
