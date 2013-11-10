#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from django.template import RequestContext
from models import UploadFile, Barcode, Comments
from goods_uncover.settings import STATICFILES_DIRS
from forms import UploadForm
from django.contrib import messages
from misc.pipline import barcode_search

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


def addfile(request):
    #if not request.user.is_authenticated():
     #   return HttpResponseRedirect('/login/')
    if request.method == 'POST': 
        uploadform = UploadForm(request.POST or None, request.FILES or None)
        if uploadform.is_valid():
            f =request.FILES['File']            
            
            new_file = UploadFile(FileName=f.name,File=f)
            new_file.save()

            #data = ' '.join(barcode_search(STATICFILES_DIRS[0] + str(new_file.File)))

            dct_data = barcode_search(STATICFILES_DIRS[0] + str(new_file.File))
            os.remove(STATICFILES_DIRS[0] + str(new_file.File))            
            
            magic_numbers = str(dct_data['sym'])
            if request.user.is_authenticated():
                us=request.user
            else:
                us=None
            
            barcode = Barcode(FK_Owner=us,Barcode=magic_numbers,Title=dct_data['desc'][0],Description="")
            barcode.save()
            
            data = None
            if dct_data['type'] == 'google':
                data = ' '.join(dct_data['ans'])
            elif dct_data['type'] == 'ya market':
                data = ''
                for x in dct_data['ans']:
                    comments = Comments(FK_Barcode=barcode,Author=x[0],Text=x[1])
                    comments.save()
                    
                    #data += u'>>>\n %s\n%s' % (x[0], x[1])
                #data = data[:700]
            else:
                data = 'None'
            
  
        else:
            messages.error(request, "Это не изображение")
            return HttpResponseRedirect(request.META['HTTP_REFERER'])            
    else:
        uploadform = UploadForm(None, None)
#    data = ' '.join(barcode_search(STATICFILES_DIRS[0] + str(new_file.File)))
 #   template = get_template("main.html")     
 #   context = RequestContext(request, {
 #       'data' : data,
    #})
    return HttpResponseRedirect('/')


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
    
'''    
def delfile(request,file_id):
    #if not request.user.is_authenticated():
     #   return HttpResponseRedirect('/login/')
        
    try:
        del_file = UploadFile.objects.get(id=file_id)   
    except:
        messages.error(request, 'Файл не найден')
        return HttpResponseRedirect(request.META['HTTP_REFERER'])
        
    if del_file.Owner != request.user:
        messages.error(request, 'Недостаточно прав')
    else:
        if os.path.isfile(STATICFILES_DIRS[0] + str(del_file.File)):
                os.remove(STATICFILES_DIRS[0] + str(del_file.File))        
        f_name = del_file.FileName
        del_file.delete()
        messages.success(request, str(f_name) + ' был успешно удален')

            
    return HttpResponseRedirect(request.META['HTTP_REFERER'])
'''
