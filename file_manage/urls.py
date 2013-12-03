#from django.conf.urls.defaults import *
from django.conf.urls import patterns, include, url

urlpatterns = patterns('file_manage.views',
                       url(r'all/$', 'allfiles', name='file_manage.allfiles'),
                       url(r'last/$', 'last_barcode', name='file_manage.last_barcode'),
                        url(r'add/$', 'addfile', name = 'file_manage.addfile'),
                        #url(r'^(?P<nomber>\d+)/+task/',include('task.urls')),
                    )
