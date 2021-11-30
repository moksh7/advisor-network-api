from rest_framework import serializers
from authentication.models import CustomUser


class RegisterSerializer(serializers.ModelSerializer):
    '''Serializes registration request and creates a new user'''

    class Meta:
        model = CustomUser
        fields = ['id','name','email','password','token']
        extra_kwargs = {
            'password': {'write_only':True},
            'name': {'write_only':True},
            'email': {'write_only':True},
        }
        read_only_fields = ['token']


    def create(self,validated_data):
        '''Creates a new user instance'''

        return CustomUser.objects.create_user(**validated_data)

class LoginSerializer(serializers.ModelSerializer):
    '''Serializes Login Credentials and returns id and token of the user'''

    class Meta:
        model = CustomUser
        fields = ['id','email','password','token']
        extra_kwargs = {
            'password': {'write_only':True},
            'email': {'write_only':True},
        }
        read_only_fields = ['token']

   