#!/usr/bin/env python
# -*- coding:utf-8 -*-

from django import forms
from django.utils.translation import ugettext as _

class UploadForm(forms.Form):
    File = forms.ImageField(label = _(u'Файл'))
