#!/usr/bin/env python
# -*- coding:utf-8 -*-

from django.contrib import auth
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.template.loader import get_template
from django.template import RequestContext
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect
from django.views.generic.simple import direct_to_template
from forms import *

def main(request):
        return direct_to_template(request, 'main.html')

@csrf_protect
def registr(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/')
    
    errors_registr = []
    form = RegForm(request.POST or None)
    
 
    if request.method == 'POST' and form.is_valid():
        username = form.cleaned_data.get('username', None)
        password = form.cleaned_data.get('password', None)
        check_password = form.cleaned_data.get('check_password', None)        
        email = form.cleaned_data.get('email',  None)
        
        if password != check_password:
            errors_registr.append("Пароли не совпали")
        
        login = User.objects.filter(username=username)        
        if len(login) > 0:
            errors_registr.append("Имя занято")

        if errors_registr:
            return HttpResponseRedirect('/login/')
        
        user = User.objects.create_user(username, email, password)
        user.save()        
        return HttpResponseRedirect('/login/')
 
    template = get_template("registr.html")    
    context = RequestContext(request, {
        'form': form,  
        'errors':errors_registr, 
        'user': request.user
    })
       
    return HttpResponse(template.render(context))

    
def logout(request):
    if request.user.is_authenticated():
        auth.logout(request)
    response = HttpResponseRedirect('/')     
    response.delete_cookie('findPr')
    response.delete_cookie('check')    
    return response
    
@csrf_protect    
def login(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/')
    errors_login = []
    form = LoginForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        username = form.cleaned_data.get('username', None)
        password = form.cleaned_data.get('password', None)
        user = auth.authenticate(username=username, password=password)
        if user and user.is_active:
            auth.login(request, user)
            return HttpResponseRedirect('/')
        else:
            errors_login.append("Неверное имя или пароль")
   
    template = get_template("login.html")    
    context = RequestContext(request, {
        'form': form,  
        'errors':errors_login, 
        'user': request.user
    })
       
    return HttpResponse(template.render(context))
