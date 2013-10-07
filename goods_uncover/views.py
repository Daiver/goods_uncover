#!/usr/bin/env python
#-*- coding:utf-8 -*-
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from django.template import RequestContext

def main_page(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/files/all/')
    print "222"        
    template = get_template("main.html")
    context = RequestContext(request, {
    })
    return HttpResponse(template.render(context))
    

def test(request):
    print "test"
    template = get_template("test.html")
    context = RequestContext(request, {
    })
    return HttpResponse(template.render(context))
