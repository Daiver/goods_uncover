#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import RequestContext
from django.http import HttpResponseRedirect
from models import UploadFile
from goods_uncover.settings import STATICFILES_DIRS
from forms import UploadForm
from django.contrib import messages

def allfiles(request):
    
    files = UploadFile.objects.all()
    #print files
    uploadform = UploadForm(None, None)
    template = get_template("main.html")
    context = RequestContext(request, {
        'files' : files,
        'uploadform' : uploadform,
    })
    return HttpResponse(template.render(context))


def addfile(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/welcome/')
    if request.method == 'POST': 
        uploadform = UploadForm(request.POST or None, request.FILES or None)
        if uploadform.is_valid():
            f =request.FILES['File']            
            new_file = UploadFile(FileName=f.name,Owner=request.user,File=f)
            new_file.save()
    else:
        uploadform = UploadForm(None, None)

    template = get_template("main.html")     
    context = RequestContext(request, {
        'data' : data,
    })
    return HttpResponse(template.render(context))
 
    
def delfile(request,file_id):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/welcome/')
        
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