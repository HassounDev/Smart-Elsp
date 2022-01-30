from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.Merchandise)
admin.site.register(models.Orderer)
admin.site.register(models.LoadUnit)
admin.site.register(models.Tag)
admin.site.register(models.Product)
admin.site.register(models.MerchandiseDoc)
