from django.contrib import admin
from vendors.models import Vendor
from django.forms import TextInput, Textarea
from django.db import models

# Register your models here.

# class VendorAdmin(admin.ModelAdmin):
#     formfield_overrides = {
#         models.CharField: {'widget': TextInput(attrs={'size':'20'})},
#         models.TextField: {'widget': Textarea(attrs={'rows':4, 'cols':40})},
#     }

admin.site.register(Vendor)