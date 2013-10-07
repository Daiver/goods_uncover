#!/usr/bin/env python
# -*- coding:utf-8 -*-

from django import forms
from django.utils.translation import ugettext as _

class UploadForm(forms.Form):
    File = forms.ImageField(label = "", widget=forms.FileInput(attrs={'class':'btn btn-success btn-large','id':'file','onchange':'fileSelected(this);'}),)
    FileResize = forms.ImageField(label = "", widget=forms.FileInput(attrs={'class':'btn btn-success btn-large'}),required=False)
