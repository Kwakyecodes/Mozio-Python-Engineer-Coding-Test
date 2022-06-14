from rest_framework import viewsets 
from . import models
from . import serializers


class ServiceAreaViewset(viewsets.ModelViewSet):
    queryset = models.ServiceArea.objects.all()
    serializer_class = serializers.ServiceAreaSerializer
    
    
class ProviderViewset(viewsets.ModelViewSet):
    queryset = models.Provider.objects.all()
    serializer_class = serializers.ProviderSerializer