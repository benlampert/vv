from django.contrib import admin
from deals.models import Site, Size, IabMainCategory, IabSubCategory, PriceModels, DealTypes, Deals, Publisher
# Register your models here.

admin.site.register(Site)
admin.site.register(Size)
admin.site.register(IabMainCategory)
admin.site.register(IabSubCategory)
admin.site.register(PriceModels)
admin.site.register(DealTypes)
admin.site.register(Deals)
admin.site.register(Publisher)