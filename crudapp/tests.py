from rest_framework.test import APITestCase
from rest_framework import status
import json

from .models import Provider


class ProviderTestCase(APITestCase):
    
    body = {'name': 'testName', 
            'email':'test@gmail.com',
            'phone_number':'+233000000000',
            'language': 'English',
            'currency': 'USD'}
    
    def temp_provider_id(self):
        '''
        Creates temporary provider and returns it's id
        '''
        temp_post = self.client.post('/api/provider/', self.body)
        temp_provider = self.client.get('/api/provider/', self.body)
        return  temp_provider.json()[0]['id']
        
    def test_valid_post(self):
        response = self.client.post('/api/provider/', self.body)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
    def test_valid_retrieve(self):
        response = self.client.get('/api/provider/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_valid_update(self):
        response = self.client.put(f'/api/provider/{self.temp_provider_id()}/', self.body)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_valid_delete(self):
        response = self.client.delete(f'/api/provider/{self.temp_provider_id()}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        
        

class ServiceAreaTestCase(APITestCase):
    
    provider_body = {'name': 'testName', 
                    'email':'test@gmail.com',
                    'phone_number':'+233000000000',
                    'language': 'English',
                    'currency': 'USD'}
   
    servicearea_body = {'name': 'testName',
                        'price': '22.50',
                        'polygon': 'SRID=4326;POLYGON ((0 0, 0 50, 50 50, 50 0, 0 0))'
        }
    
    def temp_servicearea_body(self):
        '''
        Creates a tempoary provider, get it's id and returns a complete servicearea body
        '''
        temp_post = self.client.post('/api/provider/', self.provider_body)
        temp_provider = self.client.get('/api/provider/', self.provider_body)
        
        localbody = self.servicearea_body
        localbody['provider'] = temp_provider.json()[0]['id']
        
        return localbody
    
    def temp_service_area_id(self):
        '''
        Creates a temporary servicearea and returns it's id
        '''
        temp_post = self.client.post('/api/servicearea/', self.temp_servicearea_body())
        temp_servicearea = self.client.get(f'/api/servicearea/')
        return temp_servicearea.json()[0]['id']
        
    def test_valid_post(self):
        response = self.client.post('/api/servicearea/', self.temp_servicearea_body())
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
    def test_valid_retrieve(self):
        response = self.client.get(f'/api/servicearea/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_valid_update(self):
        response = self.client.put(f'/api/servicearea/{self.temp_service_area_id()}/', self.temp_servicearea_body())
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_valid_delete(self):
        response = self.client.delete(f'/api/provider/{self.temp_service_area_id()}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        
        
        
class ValidSericeAreasTestCase(APITestCase):
    
    body = {'lat': 23,
            'lng': 25}
    
    
    def test_valid_post(self):
        response = self.client.post('/fetch/', json.dumps(self.body), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_invalid_post(self):
        response = self.client.post('/fetch/', json.dumps({}), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)