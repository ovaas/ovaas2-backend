from rest_framework import generics, permissions

# Create your views here.
from .models import DemoInfo, DeployStatus
from .serializers import DemoInfoSerializer, DeployStatusSerializer


class DeployStatusAPIView(generics.ListAPIView):
    queryset = DeployStatus.objects.all()
    serializer_class = DeployStatusSerializer
    permission_classes = [permissions.IsAuthenticated]


class DemoListAPIView(generics.ListAPIView):
    queryset = DemoInfo.objects.all()
    serializer_class = DemoInfoSerializer
