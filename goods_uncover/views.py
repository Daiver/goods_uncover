#!/usr/bin/env python
#-*- coding:utf-8 -*-
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from django.template import RequestContext

from file_manage.models import UploadFile, Barcode
from goods_uncover.settings import STATICFILES_DIRS
from file_manage.forms import UploadForm
from django.contrib import messages


def main_page(request):
    
    #if request.user.is_authenticated():
    #    return HttpResponseRedirect('/files/all/')
    #print "222"        
#    template = get_template("main.html")
#    context = RequestContext(request, {
#    })
#    return HttpResponse(template.render(context))
    
    files = UploadFile.objects.all()
    barcode = Barcode.objects.all()#filter(FK_UploadFile__Owner=request.user).order_by("-FK_UploadFile__Uploaded_date")    
    
    uploadform = UploadForm(None)
    template = get_template("main.html")
    context = RequestContext(request, {
        'files' : files,
        'uploadform' : uploadform,
        'image' : barcode[0].FK_UploadFile,
        'data' : barcode[0].Data,
        'barcode' : barcode[0].Barcode,
    })
    return HttpResponse(template.render(context))



def test(request):
    print "test"
    template = get_template("test.html")
    context = RequestContext(request, {
    })
    return HttpResponse(template.render(context))
