from django.views import View
from django.contrib.auth import authenticate,login,get_user
from django.http import HttpResponseBadRequest,HttpResponseForbidden,JsonResponse
from django.core.cache import cache

from rest_framework.authtoken.models import Token


class AuthUser(View):
    def get(self,request,*args,**kwargs):
        # reject the get request and return response code 400
        return HttpResponseBadRequest

    def post(self,request):
        self.token = 0 #！need rewrite
        
        
        # first,check the session
        if request.session:
            self.user_obj = request.user
            
        # or,check the access token
        
        # elif request.COOKIES['access_token']:
        #     self.user_obj = self._check_token(request,request.COOKIES['access_token'])
             
        # or,check the username and password          
        elif request.POST['password']:
            self.user_obj = self._auth_password(request)

        else:
            return HttpResponseBadRequest
        
        if self.user_obj:
            self._login(request,self.user_obj)
            return self._response()
        else:
            return HttpResponseForbidden


    def _auth_password(self,request):
        username = request.POST['user']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        return user
        
    
    def _create_token(self,user):
        try:
            Token.objects.filter(user=user).delete()
        finally:
            token = Token.objects.create(user=user)
            return token

    def _check_token(self,request,token):
        # TODO
        #return user
        pass

    def _login(self,request,user=None):
        login(request,user)

    def _response(self):

        CookieAge = 60 * 60 * 24 * 7 # 7days
        
        acess_token = self.token
        
        response = JsonResponse(acess_token,status_code=200)
        response.set_cookie(acess_token,max_age=CookieAge,secure=True)

        return response