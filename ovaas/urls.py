from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('apiv1.urls')),
    path('api/token/', TokenObtainPairView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)