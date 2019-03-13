from django.contrib.gis.db import models


class CostCenter(models.Model):
    name = models.CharField(max_length=75)
    coordinates = models.PointField()

    def __str__(self):
        return self.name

