from django.conf.urls.defaults import *
from django.conf.urls import patterns, include, url

urlpatterns = patterns('file_manage.views',
                       url(r'all/$', 'allfiles', name='file_manage.allfiles'),
                        url(r'add/$', 'addfile', name = 'file_manage.addfile'),
                        url(r'del/(?P<file_id>\d+)/$', 'delfile', name = 'file_manage.delfile'),
                        #url(r'^(?P<nomber>\d+)/+task/',include('task.urls')),
                    )