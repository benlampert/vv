from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.db.models import Sum

from evaluations.models import Evaluations, Section, Question, VendorEvaluation, MT_VendorAnswers

# Create your views here.
class EvaluationListView(generic.ListView):
    template_name = 'evaluations/vendor_eval_list.html'
    context_object_name = 'vendor_eval_list'

    def get_queryset(self):
        """Return all the evaluations."""
        return MT_VendorAnswers.objects.values('vendor__vendor_name', 'vendor__id').order_by('vendor_id').distinct()
        
# class EvaluationDetailView(generic.DetailView):
#     template_name = 'evaluations/vendor_eval_details.html'
#     context_object_name = 'answers'

#     def get_queryset(self):
#         """Return all the evaluations."""
#         return MT_VendorAnswers.objects.values('question__eval_question_name').order_by('question_id').distinct()

class EvaluationDetailView(generic.ListView):
    template_name = 'evaluations/vendor_eval_table.html'
    context_object_name  = 'vendor_eval_details'
    
    def get_queryset(self):
        return MT_VendorAnswers.objects.values('vendor__vendor_name', 'question__eval_question_name', 'answer', 'question__eval_section__section_name').order_by('vendor__vendor_name')

class EvaluationCategoryIndexView(generic.ListView):
    template_name = 'evaluations/vendor_eval_cat_table.html'
    context_object_name = 'vendor_eval_cat'
    
    def get_queryset(self):
        return MT_VendorAnswers.objects.values('vendor__vendor_name', 'question__eval_section__section_name').annotate(score=Sum('answer')).order_by('vendor')
    