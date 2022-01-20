from rest_framework.views import APIView
from rest_framework.response import Response
from student import models
from student.serializers import StudentSerializer
from rest_framework import status

class GetStudent(APIView):
  def get(self,request):
    students_obj= models.Student.objects.all()
    serializer_obj1= StudentSerializer(students_obj,many=True)
    return Response(serializer_obj1.data,status=status.HTTP_200_OK)

  def post(self,request):
    serializer_obj2=StudentSerializer(data=request.data)
    if serializer_obj2.is_valid():
      serializer_obj2.save()
      return Response(serializer_obj2.data,status=status.HTTP_201_CREATED)
    return Response(serializer_obj2.errors,status=status.HTTP_400_BAD_REQUEST)

class UpdateDelStudent(APIView):
  def get_object(self,id):
    try:
      return models.Student.objects.get(id=id)
    except models.Student.DoesNotExist:
      return Response(status=status.HTTP_400_BAD_REQUEST)
  
  def get(self,request,id):
    stu_obj=self.get_object(id)
    serializer_obj3=StudentSerializer(stu_obj)
    return Response(serializer_obj3.data)
  
  def put(self,request,id):
    stu_obj=self.get_object(id)
    serializer_obj4=StudentSerializer(stu_obj,data=request.data)
    if serializer_obj4.is_valid():
      serializer_obj4.save()
      return Response(serializer_obj4.data,status=status.HTTP_200_OK)
    return Response(serializer_obj4.errors)
  
  def delete(self,request,id):
    stu_obj=self.get_object(id)
    stu_obj.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
    







