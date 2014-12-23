from django.contrib import admin
from vendors.models import Vendor, Inventory, Data_Source, Adserver
from django.forms import TextInput, Textarea
from django.db import models

# Register your models here.
admin.site.register(Vendor)
admin.site.register(Inventory)
admin.site.register(Data_Source)
admin.site.register(Adserver)