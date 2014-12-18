from django.db import models
from django.utils import timezone

# Create your models here.
class Vendor(models.Model):
    vendor_name = models.CharField(max_length=200)
    added_date = models.DateTimeField('date_added', default=timezone.now())

    def __str__(self):
        return self.vendor_name

