import time
import jwt
from ovaas_backend_django.settings import SECRET_KEY
from rest_framework.authentication import BaseAuthentication
from rest_framework import exceptions
import logging

from auth_parts.models import UserInfo

class NormalAuthentication(BaseAuthentication):
    def authenticate(self, request):
        username = request._request.POST.get("username")
        password = request._request.POST.get("password")
        user_obj = UserInfo.objects.filter(username=username).first()
        logging.info(user_obj)
        if not user_obj:
            raise exceptions.AuthenticationFailed('Auth is failed')
        elif user_obj.password != password:
            raise exceptions.AuthenticationFailed('Password is not much')
        token = generate_jwt(user_obj)
        return (token, None)

    def authenticate_header(self, request):
        pass

def generate_jwt(user):
    timestamp = int(time.time()) + 60*60*24*7
    return jwt.encode(
        {"userid": user.pk, "username": user.username, "exp": timestamp},
        SECRET_KEY)