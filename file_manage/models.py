# -*- coding:utf-8 -*-

from django.db import models
from django.contrib.auth.models import User


def make_upload_path(instance, filename):
    """Generates upload path for FileField"""
    return u"uploads/temp/%s" % (filename)

class UploadFile(models.Model):
    FileName = models.CharField(max_length=255)
    File = models.ImageField(upload_to=make_upload_path)
    Uploaded_date = models.DateTimeField(auto_now_add=True)

class Barcode(models.Model):
    FK_Owner = models.ForeignKey(User)
    Barcode = models.CharField(max_length=16)
    Data = models.TextField(max_length=1000)