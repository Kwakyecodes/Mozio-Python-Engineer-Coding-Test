from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest
from django.contrib.gis.geos import Point
from rest_framework.decorators import api_view
import json

from .models import Provider, ServiceArea


@api_view(['POST'])
def valid_service_areas(request):
    '''
    Api point that takes lat/lng pair and returns all service areas containing the pair and their provider's name
    Method: POST
    Accepts: Application/json
    '''
    if request.method == 'POST':
        location_details = json.loads(request.body)
        
        try:
            lat = location_details["lat"]
        except:
            return HttpResponseBadRequest('Error: Body must contain a latitude point')
        
        try:
            lng = location_details["lng"]
        except:
            return HttpResponseBadRequest('Error: Body must contain a longitude point')
        
        try:
            point = Point([lat, lng])
        except:
            return HttpResponseBadRequest('Error: Invalid values for latitude and longitude points')
        
        areas_info = list(ServiceArea.objects.filter(polygon__contains=point).values('name', 'provider_id', 'price'))
        
        for area_info in areas_info:
            area_info['provider_name'] = Provider.objects.get(id=area_info['provider_id']).name
            del area_info['provider_id']
        
        return JsonResponse(areas_info, safe=False)