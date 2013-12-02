from django.conf.urls import patterns, include, url
from views import *
from auth.views import * 
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^yandex/(?P<barcode>\d+)/+$', yandex_search),
    url(r'^softmarket/(?P<barcode>\d+)/+$', softmarket_search),
    
    url(r'^$', main_page2),    
    url(r'^registr/$', registr),
    url(r'^login/$', login),
    url(r'^logout/$', logout),
    url(r'^test/$', test),


     url(r'^files/',include('file_manage.urls')),
    # Examples:
    # url(r'^$', 'goods_uncover.views.home', name='home'),
    # url(r'^goods_uncover/', include('goods_uncover.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
