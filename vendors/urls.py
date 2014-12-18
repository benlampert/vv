from django.conf.urls import patterns, url

from vendors import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='vendors'),
    url(r'^(?P<vendor_id>\d+)/$', views.detail, name='detail'),
)