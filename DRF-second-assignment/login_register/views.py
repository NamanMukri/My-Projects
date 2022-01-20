from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from login_register.serializers import UserSerializer
from rest_framework.authtoken.models import Token
#from django.contrib.auth.models import User

class CreateUserView(APIView):
  
  def post(self,request):
    serializer_obj2=UserSerializer(data=request.data)
    if serializer_obj2.is_valid():      
      serializer_obj2=serializer_obj2.save()
      token,created=Token.objects.get_or_create(user=serializer_obj2)
      serializer_obj2.check_password(request.data['password'])
      return Response(data={"id":serializer_obj2.id,"username":serializer_obj2.username,"email":serializer_obj2.email,"token":token.key},status=status.HTTP_201_CREATED)
    return Response(data=serializer_obj2.errors,status=status.HTTP_400_BAD_REQUEST)
      
      