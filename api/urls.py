from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import DemoListAPIView, DeployStatusAPIView


urlpatterns = [
    path('demo/', DemoListAPIView.as_view()),
    path('deploy/status/', DeployStatusAPIView.as_view()),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
