from django.conf.urls import patterns, url

from vendors import views

urlpatterns = patterns('',
    #url(r'^$', views.IndexView, name='index'),
    url(r'^$', views.VendorListView.as_view(), name='vendors'),    
    url(r'^vendors/$', views.VendorListView.as_view(), name='vendors'),
    url(r'^vendors/vv$', views.VendorVVListView.as_view(), name='vv_vendors'),
    url(r'^(?P<pk>\d+)/$', views.VendorDetailView.as_view(), name='detail'),
    url(r'^data/$', views.DataListView.as_view(), name='data'),
    url(r'^data/(?P<pk>\d+)/$', views.DataDetailView.as_view(), name='data_detail'),
    url(r'^inventory/$', views.InventoryListView.as_view(), name='inventory'),
    url(r'^inventory/(?P<pk>\d+)/$', views.InventoryDetailView.as_view(), name='inventory_detail'),
    url(r'^adserver/(?P<pk>\d+)/$', views.AdserverDetailView.as_view(), name='adserver_detail'),
)   