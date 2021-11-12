from django.contrib import admin

from .models import DemoInfo, DeployStatus


admin.site.register(DemoInfo)
admin.site.register(DeployStatus)