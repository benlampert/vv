from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

from deals.models import Sites, Size, IabMainCategory, IabSubCategory, PriceModels, Publisher

#Create your views here.
class SitesListView(generic.ListView):
    template_name = 'deals/deals_list.html'
    context_object_name = 'pubs_list'

    def get_queryset(self):
        """Return the last five published vendors."""
        return Sites.objects.order_by('site_name')


class SitesDetailView(generic.DetailView):
    model = Sites
    template_name = 'deals/deal_detail.html'
