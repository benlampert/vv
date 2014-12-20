from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

from vendors.models import Vendor, Inventory
# Create your views here.

# class IndexView(generic.ListView):
#     template_name = 'vendors/index.html'
#     context_object_name = 'latest_vendor_list'

class VendorListView(generic.ListView):
    template_name = 'vendors/vendors.html'
    context_object_name = 'latest_vendor_list'

    def get_queryset(self):
        """Return the last five published vendors."""
        return Vendor.objects.order_by('-added_date')[:5]


class VendorDetailView(generic.DetailView):
    model = Vendor
    template_name = 'vendors/detail.html'

class InventoryListView(generic.ListView):
    template_name = 'vendors/inventory.html'
    context_object_name = 'inventory_sources'
    
    def get_queryset(self):
        return Inventory.objects.all()
    
    # def get_integrated_vendors(self)
    #     sources = Inventory.objects.all()
        
    #     return Inventory.objects.vendor_set.all()


