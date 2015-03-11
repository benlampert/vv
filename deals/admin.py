from django.contrib import admin
from deals.models import Sites, Size, IabMainCategory, IabSubCategory, PriceModels, Publisher
# Register your models here.

admin.site.register(Sites)
admin.site.register(Size)
admin.site.register(IabMainCategory)
admin.site.register(IabSubCategory)
admin.site.register(PriceModels)
admin.site.register(Publisher)