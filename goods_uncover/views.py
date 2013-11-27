#!/usr/bin/env python
#-*- coding:utf-8 -*-
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from django.template import RequestContext

from file_manage.models import UploadFile, Barcode, Comments
from goods_uncover.settings import STATICFILES_DIRS
from file_manage.forms import UploadForm, CheckedForm, CommentForm
from django.contrib import messages

from django.core.paginator import Paginator,EmptyPage, PageNotAnInteger


def main_page(request, barcode):
    descr = None
    barcode = Barcode.objects.filter(Barcode=barcode)#all().order_by("-id")#filter(FK_UploadFile__Owner=request.user).order_by("-FK_UploadFile__Uploaded_date")    
    if barcode:
        barcode = barcode[0]
        descr = barcode.Description.split('|||')    

    else:
        barcode = Barcode()
    active = ["active",""]
    if request.session.get('find', False):
        if request.session["find"]:
            active = []
            active.append("")
            active.append("active")
        request.session["find"] = False
            
    
    comments = Comments.objects.filter(FK_Barcode=barcode)

    paginator = Paginator(comments, 4) # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        ms = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        ms = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        ms = paginator.page(paginator.num_pages)    
    
    uploadform = UploadForm(None)
    checkedform = CheckedForm(None)
    commentform = CommentForm(None)
    template = get_template("main.html")
    context = RequestContext(request, {
        'uploadform' : uploadform,
        'checkedform' : checkedform,
        'commentform': commentform,
        'ms' : ms,
        'title' : barcode.Title,
        'comments': comments,
        'barcode' : barcode.Barcode,
        'data': descr,
        'active': active,
    })
    return HttpResponse(template.render(context))

def main_page2(request):
    
    barcode = 0#Barcode.objects.order_by("-id")#filter(FK_UploadFile__Owner=request.user).order_by("-FK_UploadFile__Uploaded_date")    
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
        request.session["find"] = False
            
    
    comments = Comments.objects.filter(FK_Barcode=barcode)
    uploadform = UploadForm(None)
    checkedform = CheckedForm(None)
    template = get_template("main.html")
    context = RequestContext(request, {
        'uploadform' : uploadform,
        'checkedform' : checkedform,
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
