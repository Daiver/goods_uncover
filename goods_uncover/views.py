#!/usr/bin/env python
#-*- coding:utf-8 -*-
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from django.template import RequestContext

from file_manage.models import UploadFile, Barcode, Comments
from goods_uncover.settings import STATICFILES_DIRS
from file_manage.forms import UploadForm
from django.contrib import messages



def main_page(request):
    
    barcode = Barcode.objects.all().order_by("-id")#filter(FK_UploadFile__Owner=request.user).order_by("-FK_UploadFile__Uploaded_date")    
    if barcode:
        barcode = barcode[0]
    else:
        barcode = Barcode()
    active = ["active",""]
    if request.session.get('find', False):
        if request.session["find"]:
            active = []
            active.append("")
            active.append("active")
            
    
    comments = Comments.objects.filter(FK_Barcode=barcode)
    uploadform = UploadForm(None)
    template = get_template("main.html")
    context = RequestContext(request, {
        'uploadform' : uploadform,
        'title' : barcode.Title,
        'comments': comments,
        'barcode' : barcode.Barcode,
        'active': active,
    })
    return HttpResponse(template.render(context))




def test(request):
    print "test"
    template = get_template("test.html")
    context = RequestContext(request, {
    })
    return HttpResponse(template.render(context))
