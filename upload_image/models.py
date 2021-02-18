from django.db import models
import time


class UploadImage(models.Model):
    image = models.ImageField(upload_to='', blank=True, null=True)