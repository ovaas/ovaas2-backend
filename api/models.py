from django.db import models

# Create your models here.


class DemoInfo(models.Model):
    app_name = models.CharField(max_length=128)
    app_name_en = models.CharField(max_length=128)
    description = models.TextField()
    description_en = models.TextField()
    thumbnail_url = models.CharField(max_length=128)
    page_url = models.CharField(max_length=128)


class DeployStatus(models.Model):
    status = models.CharField(max_length=10)
    message = models.CharField(max_length=50)
