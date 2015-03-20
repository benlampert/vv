from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

from vendors.models import Vendor, Inventory, Data_Source, Adserver
# from evaluations.models import MT_VendorAnswers
# Create your views here.
# class IndexView(generic.ListView):

#     template_name = 'vendors/index.html'
#     context_object_name = 'latest_vendor_list'

class VendorListView(generic.ListView):
    template_name = 'vendors/vendors.html'
    context_object_name = 'latest_vendor_list'

    def get_queryset(self):
        
        return Vendor.objects.order_by('vendor_name')

class VerifiedVendorListView(generic.ListView):
    template_name = 'vendors/verified_vendors.html'
    context_object_name = 'verified_vendors'

    def get_queryset(self):
        
        return Vendor.objects.filter(vv_contract=1).order_by('vendor_name')

class VendorDetailView(generic.DetailView):
    model = Vendor
    template_name = 'vendors/detail.html'

class InventoryListView(generic.ListView):
    template_name = 'vendors/inventory.html'
    context_object_name = 'inventory_sources'
    
    def get_queryset(self):
        return Inventory.objects.order_by('inventory_name')

class DataListView(generic.ListView):
    template_name = 'vendors/data.html'
    context_object_name = 'data_sources'
    
    def get_queryset(self):
        return Data_Source.objects.all()


class InventoryDetailView(generic.DetailView):
    model = Inventory
    template_name = 'vendors/inventory_detail.html'
    
class DataDetailView(generic.DetailView):
    model = Data_Source
    template_name = 'vendors/data_detail.html'
    
class AdserverDetailView(generic.DetailView):
    model = Adserver
    template_name = 'vendors/adserver_detail.html'
