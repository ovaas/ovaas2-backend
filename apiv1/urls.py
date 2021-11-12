from django.urls import path
from .views import DemoListAPIView, DeployStatusAPIView


urlpatterns = [
    path('demo/', DemoListAPIView.as_view()),
    path('deploy/status/', DeployStatusAPIView.as_view()),
]