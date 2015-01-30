from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'vv.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^', include('vendors.urls')),
    url(r'^vendors/', include('vendors.urls')),
    url(r'^inventory/', include('vendors.urls')),
    url(r'^data/', include('vendors.urls')),
    url(r'^evaluations/', include('evaluations.urls')),
    url(r'^deals/', include('deals.urls')),
    url(r'^table/', include('tabletest.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
