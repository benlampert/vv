from django.db import models
from vendors.models import Vendor, Inventory
from django.utils import timezone

# Create your models here.

class Size(models.Model):
    size_name = models.CharField(max_length=200)

    def __str__(self):
        return self.size_name
    
    class Meta:
        verbose_name = "Size"
        verbose_name_plural = "Sizes"

class IabMainCategory(models.Model):
    iab_main_category_name = models.CharField(max_length=200)

    def __str__(self):
        return self.iab_main_category_name
    
    class Meta:
        verbose_name = "IAB Main Category"
        verbose_name_plural = "IAB Main Categories"
		
class IabSubCategory(models.Model):
    iab_sub_category_name = models.CharField(max_length=200)
    iab_main_category = models.ForeignKey(IabMainCategory, related_name="iab_main_category")

    def __str__(self):
        return "%s - %s" % (self.iab_main_category, self.iab_sub_category_name)
    
    class Meta:
        verbose_name = "IAB Sub Category"
        verbose_name_plural = "IAB Sub Categories"
		

class PriceModels(models.Model):
	price_model_name = models.CharField(max_length=200)

	def __str__(self):
		return self.price_model_name

	class Meta:
		verbose_name = "Price Model"
		verbose_name_plural = "Price Models"

class DealTypes(models.Model):
	deal_type_name = models.CharField(max_length=200)

	def __str__(self):
		return self.deal_type_name

	class Meta:
		verbose_name = "Deal Type"
		verbose_name_plural = "Deal Types"

 
class Publisher(models.Model):
    publisher_name = models.CharField(max_length=200)
    integrated_conduits = models.ManyToManyField(Inventory)
    
    
    def __str__(self):
        return self.publisher_name
    
    # def was_added_recently(self):
    #     now = timezone.now()
    #     return now - datetime.timedelta(days=1) <= self.added_date <= now
    
    class Meta:
        verbose_name = "Publishers"
        verbose_name_plural = "Publishers" 
        
class Site(models.Model):
    site_name = models.CharField(max_length=200)
    publisher = models.ForeignKey(Publisher, related_name="publisher")
    iab_category = models.ManyToManyField(IabMainCategory)
    available_sizes = models.ManyToManyField(Size)
    aod_wide_deals = models.BooleanField('AOD-wide Deals Available', default=0)
   

    def __str__(self):
    	return self.site_name
    
    class Meta:
    	verbose_name = "Site"
    	verbose_name_plural = "Sites"
    	

class Deals(models.Model):
	deal_name = models.CharField(max_length=200)
	deal_ID_input = models.CharField(max_length=200)
	site_name = models.ForeignKey(Site, related_name="deal_site")
	size = models.ForeignKey(Size, related_name="sizes")
	price_model= models.ForeignKey(PriceModels, related_name="price_models")
	price_q1 = models.DecimalField(max_digits=6, decimal_places=2,default=0.00)
	price_q2 = models.DecimalField(max_digits=6, decimal_places=2,default=0.00)
	price_q3 = models.DecimalField(max_digits=6, decimal_places=2,default=0.00)
	price_q4 = models.DecimalField(max_digits=6, decimal_places=2,default=0.00)
	integrated_dsp = models.ForeignKey(Vendor, related_name="dsp")
	integrated_conduit = models.ForeignKey(Inventory, related_name="conduit")
	deal_type = models.ForeignKey(DealTypes, related_name="deal_types")
	is_aod_wide = models.BooleanField('AOD-wide Deal', default=0)


	def __str__(self):
		return "%s - %s - %s - %s - %s" % (self.site_name, self.deal_name, self.size, self.integrated_dsp, self.integrated_conduit)

	class Meta:
		verbose_name = "Deal"
		verbose_name_plural = "Deals"
  

       