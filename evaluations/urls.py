from django.conf.urls import patterns, url
from evaluations import views

urlpatterns = patterns('',

    url(r'^$', views.EvaluationDetailView.as_view(), name='evals'),
    url(r'^(?P<pk>\d+)/$', views.EvaluationDetailView.as_view(), name='eval_details'),
)