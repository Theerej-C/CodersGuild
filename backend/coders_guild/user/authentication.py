import jwt
from rest_framework.authentication import BaseAuthentication
from rest_framework import exceptions
from django.conf import settings
from .database import user_collection
from rest_framework.permissions import AllowAny
class SafeJWTAuthentication(BaseAuthentication):
    def authenticate(self, request):
        authorization_heaader = request.headers.get('Authorization')
        if not authorization_heaader:
            return None
        try:
            # header = 'Token xxxxxxxxxxxxxxxxxxxxxxxx'
            access_token = authorization_heaader.split(' ')[1]
            payload = jwt.decode(access_token, settings.SECRET_KEY, algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise exceptions.AuthenticationFailed('access_token expired')
        except IndexError:
            raise exceptions.AuthenticationFailed('Token prefix missing')
        user = user_collection.find_one({"user_name":payload['user_name']})
        if user is None:
            raise exceptions.AuthenticationFailed('User not found')
        user_model = lambda: None
        user_model.is_authenticated = True
        return (user_model, None)