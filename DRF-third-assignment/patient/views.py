from rest_framework.views import APIView
from rest_framework.response import Response
from patient import models
from patient.serialize import PatientSerializer
from rest_framework import status

class GetPatient(APIView):
  def get(self,request):
    patient_obj= models.Patient.objects.all()
    serializer_obj1= PatientSerializer(patient_obj,many=True)
    return Response(serializer_obj1.data,status=status.HTTP_200_OK)

  def post(self,request):
    serializer_obj2=PatientSerializer(data=request.data)
    if serializer_obj2.is_valid():
      serializer_obj2.save()
      return Response(serializer_obj2.data,status=status.HTTP_201_CREATED)
    return Response(serializer_obj2.errors,status=status.HTTP_400_BAD_REQUEST)

class UpdateDelPatient(APIView):
  def get_object(self,id):
    try:
      return models.Patient.objects.get(id=id)
    except models.Patient.DoesNotExist:
      return Response(status=status.HTTP_400_BAD_REQUEST)
  
  def get(self,request,id):
    patient_obj=self.get_object(id)
    serializer_obj3=PatientSerializer(patient_obj)
    return Response(serializer_obj3.data)
  
  def put(self,request,id):
    patient_obj=self.get_object(id)
    serializer_obj4=PatientSerializer(patient_obj,data=request.data)
    if serializer_obj4.is_valid():
      serializer_obj4.save()
      return Response(serializer_obj4.data,status=status.HTTP_200_OK)
    return Response(serializer_obj4.errors)
  
  def delete(self,request,id):
    patient_obj=self.get_object(id)
    patient_obj.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)