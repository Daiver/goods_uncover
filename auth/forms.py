#!/usr/bin/env python
# -*- coding:utf-8 -*-

from django import forms
from django.utils.translation import ugettext as _

class LoginForm(forms.Form):
    username = forms.CharField( label = _(u'Имя пользователя'))
    password = forms.CharField( label = _(u'Пароль'),  widget = forms.PasswordInput)
    

    
class RegForm(forms.Form):
    username = forms.CharField( label = _(u'Имя пользователя'))
    password = forms.CharField( label = _(u'Пароль'),  widget = forms.PasswordInput)
    check_password = forms.CharField( label = _(u'Повторите пароль'),  widget = forms.PasswordInput)
    email = forms.EmailField( label = _(u'Email'))

class UploadForm(forms.Form):
    File = forms.FileField(label = _(u'Файл'))
