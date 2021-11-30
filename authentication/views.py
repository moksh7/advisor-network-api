from rest_framework import serializers
from rest_framework.views import APIView
from authentication.serializers  import RegisterSerializer,LoginSerializer
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework import permissions,generics
from django.contrib.auth import get_user_model


class RegisterAdmin(APIView):
    '''Creates admin user and enforces that only 1 admin exists'''

    authentication_classes=[]

    def post(self,request,*args,**kwargs):
        if get_user_model().objects.filter(is_staff=True).count() == 0:
            serializer = RegisterSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(is_staff=True)
                return Response(serializer.data,status=status.HTTP_201_CREATED)

            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error':'Admin already exists, only 1 admin allowed'})


class Allusers(generics.ListAPIView):
    '''Retives a list of all Users accessed only the admin. '''

    permission_classes = [permissions.IsAdminUser]
    queryset = get_user_model().objects.all()
    serializer_class = RegisterSerializer


class RegisterView(APIView):
    '''creates new user instance'''

    authentication_classes=[]
    
    def post(self,request,*args,**kwargs):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)

        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    '''Verifies Login Credentials of a user and returns id and token of the user'''

    authentication_classes=[]
    
    def post(self,request,*args,**kwargs):
        email = request.data.get('email',None)
        password = request.data.get('password',None)

        user = authenticate(email=email,password=password)

        if user:
            serializer = LoginSerializer(user)
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response({'mesage':'invalid credentials'},status=status.HTTP_401_UNAUTHORIZED)