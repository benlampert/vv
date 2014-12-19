from django.db import models
from django.utils import timezone

# Create your models here.
class Vendor(models.Model):
    #picklist of vendor types
    VENDOR_TYPES = (
    ('DSP', 'Demand Side Platform'),
    ('DMP', 'Data Management Platform'),
    ('PMD', 'Preferred Marketing Developer'),
    ('SSP', 'Supply Side Platform'),
    ('PUB', 'Publisher'),
    ('DATA', 'Data Source'),
    ('ADS', 'Ad Server'),
)
    vendor_name = models.CharField(max_length=200)
    added_date = models.DateTimeField('date_added', default=timezone.now())
    vendor_type = models.CharField('vendor_type', max_length=100,choices=VENDOR_TYPES, default=('EMPTY', 'Update'))
    vv_contract = models.BooleanField('is_vv', default=0)
    vendor_blurb = models.CharField('vendor_blurb', max_length=400, default='empty')
    vendor_internal_pov = models.CharField('vendor_internal_pov', max_length=1000, default='empty')
    vendor_external_pov = models.CharField('vendor_external_pov', max_length=1000, default='empty')
    
    def __str__(self):
        return self.vendor_name
    
    def was_added_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.added_date <= now
        
