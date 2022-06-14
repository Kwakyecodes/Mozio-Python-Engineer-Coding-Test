from crudapp.viewsets import ServiceAreaViewset, ProviderViewset
from rest_framework import routers


router = routers.DefaultRouter()

router.register('servicearea', ServiceAreaViewset) # api/servicearea/
router.register('provider', ProviderViewset) # api/provider/

 
# GET, POST, PUT, DELETE