from django.conf.urls import patterns, url
from evaluations import views

urlpatterns = patterns('',

    url(r'^$', views.EvaluationDetailView.as_view(), name='evals'),
    url(r'^category/$', views.EvaluationCategoryIndexView.as_view(), name='eval_cats'),
    url(r'^marketing/$', views.EvaluationMarketingIndexView.as_view(), name='eval_marketing'),
    url(r'^(?P<pk>\d+)/$', views.EvaluationDetailView.as_view(), name='eval_details'),

)