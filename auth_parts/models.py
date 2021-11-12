from django.db import models


class UserInfo(models.Model):
    username = models.CharField(max_length=50, unique=True, db_index=True)
    password = models.CharField(max_length=100, db_index=True)