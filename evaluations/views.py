from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views.generic import ListView
from django.db.models import Sum

from evaluations.models import Evaluations, Section, Question, VendorEvaluation, MT_VendorAnswers

# Create your views here.
class EvaluationListView(ListView):
    template_name = 'evaluations/vendor_eval_list.html'
    context_object_name = 'vendor_eval_list'

    def get_queryset(self):
        """Return all the evaluations."""
        return MT_VendorAnswers.objects.values('vendor__vendor_name', 'vendor__id').order_by('vendor_id').distinct()

class EvaluationDetailView(ListView):
    template_name = 'evaluations/vendor_eval_table.html'
    context_object_name  = 'vendor_eval_details'
    
    def get_queryset(self):
        return MT_VendorAnswers.objects.values('vendor__vendor_name', 'question__eval_question_name', 'answer', 'question__eval_section__section_name').order_by('vendor__vendor_name')

class EvaluationCategoryIndexView(ListView):
    template_name = 'evaluations/vendor_eval_cat_table.html'
    context_object_name = 'vendor_eval_cat'
    
    def get_queryset(self):
        return MT_VendorAnswers.objects.values('vendor__vendor_name', 'question__eval_section__section_name').annotate(score=Sum('answer')).order_by('vendor')

class EvaluationMarketingIndexView(ListView):
    template_name = 'evaluations/vendor_eval_marketing_table.html'
    context_object_name = 'vendor_eval_marketing'
    
    def get_queryset(self):
        return MT_VendorAnswers.objects.filter(question__for_marketing=1).values('vendor__vendor_name', 'question__eval_question_name', 'answer', 'question__eval_section__section_name').order_by('vendor__vendor_name')

class VendorEvaluationListView(ListView):
    template_name = 'evaluations/vendor_eval_details.html'
    context_object_name = 'vendor_eval'
    
    def get_queryset(self):
        #self.vendor_id = get_object_or_404(MT_VendorAnswers, vendor_id=self.args[0])
        return MT_VendorAnswers.objects.filter(vendor_id=self.args[0]).order_by('question__id')#.values('vendor__vendor_name', 'question__eval_question_name', 'answer', 'question__eval_section__section_name')