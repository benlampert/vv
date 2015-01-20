from django.conf.urls import patterns, url

from deals import views

urlpatterns = patterns('',
     url(r'^$', views.DealListView.as_view(), name='deals'),
     url(r'^(?P<pk>\d+)/$', views.DealDetailView.as_view(), name='deal_detail'),
)