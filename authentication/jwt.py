from rest_framework.authentication import get_authorization_header,BaseAuthentication
from rest_framework import exceptions
from django.conf import settings
from django.contrib.auth import get_user_model
import jwt

class JWTAuthentication(BaseAuthentication):
    '''Cutom Authentication backend to support JWT'''

    def authenticate(self,request):
        auth_header = get_authorization_header(request)

        auth_data = auth_header.decode('utf-8')

        auth_token = auth_data.split(' ')

        if len(auth_token) != 2:
            raise exceptions.AuthenticationFailed('Token not valid')
        
        token = auth_token[1]
        try:
            payload = jwt.decode(token,settings.SECRET_KEY,'HS256')
            
            email = payload['email']
            user = get_user_model().objects.get(email=email)
            
            return(user,token)

        except jwt.ExpiredSignatureError:
            raise exceptions.AuthenticationFailed('Token is expired, login again')
        except jwt.DecodeError:
            raise exceptions.AuthenticationFailed('Token is invalid')
        except get_user_model().DoesNotExist:
            raise exceptions.AuthenticationFailed('User does not exist')
        



