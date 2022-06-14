from rest_framework import serializers
from .models import Provider, ServiceArea


class ServiceAreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceArea
        fields = '__all__'
        

class ProviderSerializer(serializers.ModelSerializer):
    service_area = ServiceAreaSerializer(many=True, read_only=True)
    class Meta:
        model = Provider
        fields = '__all__'