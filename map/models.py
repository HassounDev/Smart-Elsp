from django.db import models

# Create your models here.
class Map(models.Model):

    map_lat = models.CharField(u'Latitude', max_length=25, blank=True, null=True)
    map_lon = models.CharField(u'Longitude', max_length=25, blank=True, null=True)
