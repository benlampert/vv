from django.conf.urls import patterns, url
from tabletest import views

urlpatterns = patterns('',

   url(r'^$', views.people, name='tabletest'),
   
)