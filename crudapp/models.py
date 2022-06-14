from django.contrib.gis.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from phone_field import PhoneField
from django.contrib.gis.geos import Polygon
import os


class Provider(models.Model):
    name = models.CharField(max_length=100, null=True)
    email = models.EmailField(max_length = 254, null=True)
    phone_number = PhoneField(blank=True)
    langauge = models.CharField(max_length=50, null=True)
    currency = models.CharField(max_length=50)
          
    
class ServiceArea(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits = 15, decimal_places = 2)
    polygon = models.PolygonField()
    provider = models.ForeignKey(Provider, null=False, blank=False, on_delete=models.CASCADE)

@receiver(post_save, sender=Provider)
def auto_create_service_area(instance, **kwargs):
    '''
    Anytime a new provider is created, a default service area object is created for them
    '''
    service_areas = ServiceArea.objects.filter(provider=instance)
    CUSTOM_POLYGON = Polygon([[0, 0],
                                [0, 50],
                                [50, 50],
                                [50, 0],
                                [0, 0]])
    if not service_areas:
        default_service_area = ServiceArea( 
            name= os.environ.get('SERVICE_AREA_NAME'), 
            price= os.environ.get('SERVICE_AREA_PRICE'),
            polygon= CUSTOM_POLYGON,
            provider= instance)
        
        default_service_area.save()
        
        
# CRUD requests for Provider and ServiceArea
# Create / Insert / Add - POST
# Retrieve / Fetch - GET
# Update / Edit - PUT
# Delete / Remove - DELETE 