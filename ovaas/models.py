from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
User = get_user_model()


class GUIType(models.TextChoices):
    img = "image_upload", "Image Upload"
    draw = "draw", "Draw"


class Demo(models.Model):
    name_ja = models.CharField(max_length=128)
    name_en = models.CharField(max_length=128)
    description_ja = models.TextField()
    description_en = models.TextField()
    endpoint_url = models.CharField(max_length=128)
    thumbnail_uri = models.CharField(max_length=128)
    gui_type = models.CharField(max_length=128, choices=GUIType.choices)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)


class DeployStatus(models.Model):
    status = models.CharField(max_length=10)
    message = models.CharField(max_length=50)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
