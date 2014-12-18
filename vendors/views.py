from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from vendors.models import Vendor
# Create your views here.

def index(request):
    latest_vendor_list = Vendor.objects.order_by('-added_date')[:5]
    context = {'latest_vendor_list':latest_vendor_list}
    return render(request, 'vendors/index.html', context)

def detail(request, vendor_id):
    vendor = get_object_or_404(Vendor, pk=vendor_id)
    return render(request, 'vendors/detail.html', {'vendor': vendor})