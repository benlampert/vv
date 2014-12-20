from django.conf.urls import patterns, url

from vendors import views

urlpatterns = patterns('',
    # url(r'^$', views.IndexView, name='index'),
    url(r'^$', views.VendorListView.as_view(), name='vendors'),
    url(r'^(?P<pk>\d+)/$', views.VendorDetailView.as_view(), name='detail'),
)