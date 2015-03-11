from django.conf.urls import patterns, url

from deals import views

urlpatterns = patterns('',
     url(r'^$', views.SitesListView.as_view(), name='sites'),
     url(r'^(?P<pk>\d+)/$', views.SitesDetailView.as_view(), name='sites_detail'),
 )