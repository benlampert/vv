from django.db import models
from django.utils import timezone

# Create your models here.
class Inventory(models.Model):
    inventory_name = models.CharField(max_length=200)

    def __str__(self):
        return self.inventory_name
    class Meta:
        verbose_name_plural = "Inventory Sources"
        verbose_name = "Inventory Source"

class Data_Source(models.Model):
    data_source_name = models.CharField(max_length=200)

    def __str__(self):
        return self.data_source_name
    
    class Meta:
        verbose_name_plural = "Data Sources"
        verbose_name = "Data Source"

class Adserver(models.Model):
    adserver_name = models.CharField(max_length=200)

    def __str__(self):
        return self.adserver_name
    
    class Meta:
        verbose_name_plural = "Ad Servers"
        verbose_name = "Ad Server"


        
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
    added_date = models.DateTimeField('Date Added', default=timezone.now())
    vendor_type = models.CharField('Category', max_length=100,choices=VENDOR_TYPES, default=('EMPTY', 'Update'))
    vv_contract = models.BooleanField('Is Vivaki Verified', default=0)
    vv_nda = models.BooleanField('Vivaki NDA signed', default=0)
    vendor_blurb = models.TextField('Short Blurb', max_length=400, default='empty')
    vendor_internal_pov = models.TextField('Internal POV', max_length=1000, default='empty')
    vendor_external_pov = models.TextField('External POV', max_length=1000, default='empty')
    integrated_inventory_sources = models.ManyToManyField(Inventory)
    integrated_data_sources = models.ManyToManyField(Data_Source)
    integrated_adservers = models.ManyToManyField(Adserver)
    
    def __str__(self):
        return self.vendor_name
    
    # def was_added_recently(self):
    #     now = timezone.now()
    #     return now - datetime.timedelta(days=1) <= self.added_date <= now
    
    class Meta:
        verbose_name_plural = "Platforms"
        verbose_name = "Platform"