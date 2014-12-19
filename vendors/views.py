from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

from vendors.models import Vendor
# Create your views here.

class IndexView(generic.ListView):
    template_name = 'vendors/index.html'
    context_object_name = 'latest_vendor_list'

    def get_queryset(self):
        """Return the last five published vendors."""
        return Vendor.objects.order_by('-added_date')[:5]


class DetailView(generic.DetailView):
    model = Vendor
    template_name = 'vendors/detail.html'