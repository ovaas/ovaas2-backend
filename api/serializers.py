from rest_framework import serializers
from .models import DemoInfo, DeployStatus


class DemoInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DemoInfo
        fields = '__all__'


class DeployStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeployStatus
        fields = '__all__'
