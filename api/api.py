from tastypie.api import Api
from .resources import CostCenterResource


v1 = Api(api_name='v1')
v1.register(CostCenterResource())
