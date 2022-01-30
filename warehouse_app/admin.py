from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Warehouse)
admin.site.register(models.Activity)
admin.site.register(models.Building)
admin.site.register(models.Zone)
admin.site.register(models.Radius)
admin.site.register(models.Cell)
admin.site.register(models.CellType)
admin.site.register(models.Support)
admin.site.register(models.Parking)
