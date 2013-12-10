#!/usr/bin/env python
#-*- coding:utf-8 -*-
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from django.template import RequestContext

from file_manage.models import UploadFile, Barcode, CommentsYandex, CommentsSoft, BarcodeYandex, BarcodeSoft, History
from goods_uncover.settings import STATICFILES_DIRS
from file_manage.forms import UploadForm, CheckedForm, CommentForm
from django.contrib import messages

from django.core.paginator import Paginator,EmptyPage, PageNotAnInteger


def getHistory(who):
    h = []    
    if who.is_authenticated():
         h = History.objects.filter(Who=who).order_by("-Date")
    return h
    
def yandex_search(request, barcode):
    descr = None
    barcode = Barcode.objects.filter(Barcode=barcode)#all().order_by("-id")#filter(FK_UploadFile__Owner=request.user).order_by("-FK_UploadFile__Uploaded_date")    
    if barcode:
        barcode = barcode[0]
        descr = BarcodeYandex.objects.filter(FK_Barcode=barcode) #barcode.Description.split('|||')
        if descr:
            descr = descr[0].Description.split('|||')

    else:
        barcode = Barcode()
    
    active_pane = ["active",""]

    if request.session.get('find', False):
        if request.session["find"]:
            active_pane = []
            active_pane.append("")
            active_pane.append("active")
        #request.session["find"] = False
            
    active_search = ["active",""]
        
    comments = CommentsYandex.objects.filter(FK_Barcode=barcode)

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
        'active_pane': active_pane,
        'active_search': active_search,
        'history' : getHistory(request.user),
    })
    return HttpResponse(template.render(context))

def softmarket_search(request, barcode):
    descr = None
    barcode = Barcode.objects.filter(Barcode=barcode)#all().order_by("-id")#filter(FK_UploadFile__Owner=request.user).order_by("-FK_UploadFile__Uploaded_date")    
    if barcode:
        barcode = barcode[0]
        descr = BarcodeSoft.objects.filter(FK_Barcode=barcode) #barcode.Description.split('|||')    
        if descr:
            descr = descr[0].Description.split('|||')
                
    else:
        barcode = Barcode()
    active_pane = ["active",""]

    if request.session.get('find', False):
        if request.session["find"]:
            active_pane = []
            active_pane.append("")
            active_pane.append("active")
        #request.session["find"] = False
            
    active_search = ["","active"]
    comments = CommentsSoft.objects.filter(FK_Barcode=barcode)

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
        'active_pane': active_pane,
        'active_search': active_search,
       'history' : getHistory(request.user),
    })
    return HttpResponse(template.render(context))


def main_page2(request):
    
    barcode = 0#Barcode.objects.order_by("-id")#filter(FK_UploadFile__Owner=request.user).order_by("-FK_UploadFile__Uploaded_date")    
    if barcode:
        barcode = barcode[0]
    else:
        barcode = Barcode()
    active_pane = ["active",""]
    if request.session.get('find', False):
        if request.session["find"]:
            active_pane = []
            active_pane.append("")
            active_pane.append("active")
        request.session["find"] = False
            
    
    comments = []#Comments.objects.filter(FK_Barcode=barcode)
    uploadform = UploadForm(None)
    checkedform = CheckedForm(None)
    template = get_template("main.html")
    context = RequestContext(request, {
        'uploadform' : uploadform,
        'checkedform' : checkedform,
        'title' : barcode.Title,
        'comments': comments,
        'barcode' : barcode.Barcode,
        'active_pane': active_pane,
        'history' : getHistory(request.user),
    })
    return HttpResponse(template.render(context))



def test(request):
    print "test"
    template = get_template("test.html")
    context = RequestContext(request, {
    })
    return HttpResponse(template.render(context))
