from django.db import models

# Create your models here.
class Vehicle(models.Model):
    current_registration =  models.CharField(max_length=200)
    n_insurance = models.CharField(max_length=200)
    v_type = models.CharField(max_length = 200)
    v_sub_type = models.CharField(max_length = 200)
    v_place_nbr = models.IntegerField(default=0)
    v_average_consumption_city = models.FloatField()
    v_average_consumption_road = models.FloatField()
    physical_state = models.CharField(max_length = 200)
    mileage = models.FloatField()

class Container(models.Model):
    container_ref =  models.CharField(max_length=200)
    registration = models.CharField(max_length = 200)
    volume = models.FloatField()
    height = models.FloatField()
    width = models.FloatField()
    free_surface = models.FloatField()
    poid = models.FloatField()
    weight = models.FloatField()
    weight_max = models.FloatField()
    state = models.CharField(max_length = 120)
    Free_volume = models.FloatField()
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
