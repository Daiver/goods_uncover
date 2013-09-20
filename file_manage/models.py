# -*- coding:utf-8 -*-

from django.db import models
from django.contrib.auth.models import User


def make_upload_path(instance, filename):
    """Generates upload path for FileField"""
    return u"uploads/%s/%s" % (instance.Owner.username, filename)

class UploadFile(models.Model):
    Owner = models.ForeignKey(User)
    Description = models.CharField(max_length=255)
    FileName = models.CharField(max_length=255)
    File = models.ImageField(upload_to=make_upload_path)
    #Path = models.CharField(max_length=255,default=make_upload_path)
    Uploaded_date = models.DateTimeField(auto_now_add=True)

class Barcode(models.Model):
    FK_UploadFile = models.ForeignKey(UploadFile)
    Barcode = models.CharField(max_length=16)
    Data = models.TextField(max_length=1000)