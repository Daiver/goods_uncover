#-*- coding:utf-8 -*-
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import RequestContext
from file_manage.models import *

def test(request):
  
    
    template = get_template("main.html")
    context = RequestContext(request, {
    })
    return HttpResponse(template.render(context))