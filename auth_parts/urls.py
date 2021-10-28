from django.urls import path
from .views import AuthUser

urlpatterns = [
    path('',AuthUser.as_view(),name="AuthUser"),
]