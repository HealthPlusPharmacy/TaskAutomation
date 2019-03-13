from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin
from .models import CostCenter

admin.site.register(CostCenter, OSMGeoAdmin)
