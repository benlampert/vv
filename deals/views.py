from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

from deals.models import Site, Size, IabMainCategory, IabSubCategory, PriceModels, DealTypes, Deals, Publisher

# Create your views here.
class DealListView(generic.ListView):
    template_name = 'deals/deals_list.html'
    context_object_name = 'latest_deal_list'

    def get_queryset(self):
        """Return the last five published vendors."""
        return Deals.objects.order_by('deal_name')


class DealDetailView(generic.DetailView):
    model = Deals
    template_name = 'deals/deal_detail.html'
