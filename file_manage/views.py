#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template.loader import get_template
from django.template import RequestContext
from models import UploadFile, Barcode, BarcodeYandex, BarcodeSoft, CommentsYandex, CommentsSoft, History
from goods_uncover.settings import STATICFILES_DIRS
from forms import UploadForm
from django.contrib import messages
from misc.pipline import barcode_search, google_barcode_search, b_d
from  misc import ya_market, softmarket

def allfiles(request):
    
    files = UploadFile.objects.all()
    #print files
    uploadform = UploadForm(None)
    template = get_template("main.html")
    context = RequestContext(request, {
        'files' : files,
        'uploadform' : uploadform,
    })
    return HttpResponse(template.render(context))


def addHistory(barcode, who):
    if who.is_authenticated():
        if barcode:
            history = History(Who=who,What=barcode)
            history.save()

def addfile(request):
    #if not request.user.is_authenticated():
     #   return HttpResponseRedirect('/login/')
    barcode = 0
    dct_data = None
    if request.method == 'POST': 
        uploadform = UploadForm(request.POST, request.FILES)
        if uploadform.is_valid() and (request.FILES.get('File',False) or uploadform.cleaned_data.get('barcode',False)):
            dct_data = {}            
            if (request.FILES.get('File',False)):            
                f =request.FILES['File']            
                new_file = UploadFile(FileName=f.name,File=f)
                new_file.save()
                sym = b_d(STATICFILES_DIRS[0] + str(new_file.File))                
                os.remove(STATICFILES_DIRS[0] + str(new_file.File))                
                barcode = Barcode.objects.filter(Barcode=sym)
                if not barcode:
                    dct_data = barcode_search(sym)
                    sym = str(dct_data['sym'])
                    
                
            elif uploadform.cleaned_data.get('barcode',False):
                 
                sym = uploadform.cleaned_data.get('barcode',0)
                barcode = Barcode.objects.filter(Barcode=sym)               
            if not barcode:
                dct_data = barcode_search(sym)                
                magic_numbers = str(dct_data['sym'])
                if request.user.is_authenticated():
                    us=request.user
                else:
                    us=None
                
                #fix this
                descrYa = ya_market.ym_description(dct_data['modelId'][1])
                barcode = Barcode(FK_Owner=us,Barcode=magic_numbers,Title=dct_data['name'])                
                barcode.save()
                addHistory(who=request.user, barcode=barcode)                

                barcodeYa = BarcodeYandex(FK_Barcode=barcode,Description=descrYa)
                barcodeYa.save()
                
                data = None
                if dct_data['type'] == 'google':
                    data = ' '.join(dct_data['ans'])
                elif dct_data['type'] == 'ya market':
                    data = ''                                    
                    for x in dct_data['ans']:
                        commentsYa = CommentsYandex(FK_Barcode=barcode,Author=x[0],Text=x[1])
                        commentsYa.save()
                else:
                    data = 'None'
                
                
                
                #fill softmarket                
                resSo = softmarket.sf_search(dct_data['name'])                
                barcodeSo = BarcodeSoft(FK_Barcode=barcode,Description=softmarket.sf_desc(resSo[2])[0])                
                barcodeSo.save()
                comSo = softmarket.sf_reviews(resSo[2])
                for com in comSo:
                    commentsSo = CommentsSoft(FK_Barcode=barcode,Author=com[0], Text=com[1])
                    commentsSo.save()

            else:
                barcode = barcode[0]
                addHistory(who=request.user, barcode=barcode) 
            request.session["find"]=True            
            
        else:
            request.session["find"]=False
            messages.error(request, "Форма не заполнена")
            return HttpResponseRedirect("/")            
    else:
        request.session["find"]=False
        uploadform = UploadForm(None, None)
#    data = ' '.join(barcode_search(STATICFILES_DIRS[0] + str(new_file.File)))
 #   template = get_template("main.html")     
 #   context = RequestContext(request, {
 #       'data' : data,
    #})
    return HttpResponseRedirect('/yandex/' + str(barcode.Barcode))
    #return render_to_response("main.html",context_instance=RequestContext(request))

def last_barcode(request):
    uploadform = UploadForm(None,None,None)
    #last_file = UploadFile.objects.filter(Owner=request.user).order_by("-Uploaded_date")
    barcode = Barcode.objects.filter(FK_UploadFile__Owner=request.user).order_by("-FK_UploadFile__Uploaded_date")
    template = get_template("main.html")     
    context = RequestContext(request, {
        'image' : barcode[0].FK_UploadFile,
        'data' : barcode[0].Data,
        'barcode' : barcode[0].Barcode,
        'uploadform' : uploadform,
    })
    return HttpResponse(template.render(context))
    

