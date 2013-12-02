#!/usr/bin/env python
# -*- coding:utf-8 -*-

from django import forms
from django.utils.translation import ugettext as _

class UploadForm(forms.Form):
    File = forms.ImageField(label = "", widget=forms.FileInput(attrs={'class':'btn-success btn-large','id':'file'}),required=False)
   # FileResize = forms.ImageField(label = "", widget=forms.FileInput(attrs={'class':'btn btn-success btn-large','id':'hidefile'}),required=False)
    barcode = forms.CharField(label = _(u'Штрих-код: '), widget=forms.TextInput(attrs={'data-items':'4','autocomplete':'off','data-provide':'typeahead',
                            'data-source':''}),required=False)
    
class CheckedForm(forms.Form):
    check = forms.ComboField(label = _(u'Источники'), widget=forms.RadioSelect(
                                                choices=(('ya_market',_(u'Яндекс.Маркет')),('other',_(u'Другие ')))),required=False, initial=['ya_market'])
                                                
class CommentForm(forms.Form):
    author = forms.CharField(label = _(u'Автор '), widget=forms.TextInput(attrs={'data-items':'4','autocomplete':'off','data-provide':'typeahead',
                            'data-source':''}),required=False)
    text = forms.CharField(label = _(u'Комментарий '), widget=forms.Textarea(attrs={'rows':3 , 'class':'input-xlarge'}))