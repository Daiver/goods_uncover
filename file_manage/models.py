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
    FK_Owner = models.ForeignKey(User,null=True)
    Barcode = models.CharField(max_length=16)
    Title = models.CharField(max_length=100)
    #Description = models.TextField(max_length=1000)
    #Data = models.TextField(max_length=1000)

class BarcodeYandex(models.Model):
    Description = models.TextField(max_length=1000)
    FK_Barcode = models.ForeignKey(Barcode)
    
class BarcodeSoft(models.Model):
    Description = models.TextField(max_length=1000)
    FK_Barcode = models.ForeignKey(Barcode)

    
class CommentsYandex(models.Model):
    Author = models.CharField(max_length=100)
    Text = models.TextField(max_length=1000)
    FK_Barcode = models.ForeignKey(Barcode)

class CommentsSoft(models.Model):
    Author = models.CharField(max_length=100)
    Text = models.TextField(max_length=1000)
    FK_Barcode = models.ForeignKey(Barcode)
    
class CommentsGU(models.Model):
    Author = models.CharField(max_length=100)
    Text = models.TextField(max_length=1000)
    FK_Barcode = models.ForeignKey(Barcode)
