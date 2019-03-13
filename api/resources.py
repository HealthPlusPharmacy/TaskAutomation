from tastypie.resources import ModelResource
from tastypie.contrib.gis.resources import ModelResource as GeoModelResource
from locations.models import CostCenter


class CostCenterResource(GeoModelResource):
    class Meta:
        queryset = CostCenter.objects.all()
        resource_name = 'cost_center'
