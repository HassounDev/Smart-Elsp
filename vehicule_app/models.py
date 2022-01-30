from django.db import models
from django.core.urlresolvers import reverse
from position_app.models import Member


# Create your models here.
class Vehicle(models.Model):

    VEHICLE_TYPE = (('CAR','Car'),('TRUCK','Truck'),('VAN','Van'))
    VEHICLE_SOUS_TYPE = (('CAR1','Car1'),('TRUCK1','Truck1'),('VAN1','Van1'))
    member = models.ForeignKey(Member, on_delete=models.CASCADE, null=True)
    current_registration =  models.CharField(max_length=200)
    n_insurance = models.CharField(max_length=200)
    mark = models.CharField(max_length = 200)
    v_type = models.CharField(max_length = 200 , choices = VEHICLE_TYPE)
    v_sub_type = models.CharField(max_length = 200, choices = VEHICLE_SOUS_TYPE )
    v_place_nbr = models.IntegerField(default=0)
    v_average_consumption_city = models.FloatField()
    v_average_consumption_road = models.FloatField()
    physical_state = models.CharField(max_length = 200)
    mileage = models.FloatField()
    v_logo = models.FileField()


    def get_absolute_url(self):
        return reverse('vehicule_app:details', kwargs={'pk' : self.pk})

    def __str__(self):
        return self.current_registration + '-' + self.v_type


class Container(models.Model):

    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, null=True)
    container_ref =  models.CharField(max_length=200)
    registration = models.CharField(max_length = 200)
    container_type = models.CharField(max_length = 200)
    container_sub_type = models.CharField(max_length = 200)
    volume = models.FloatField()
    height_ex = models.FloatField()
    width_ex = models.FloatField()
    length_ex = models.FloatField()
    height_in = models.FloatField()
    width_in = models.FloatField()
    length_in = models.FloatField()
    #free_surface = models.FloatField()
    weight = models.FloatField()
    #weight_max = models.FloatField()
    capacity = models.FloatField()
    function = models.TextField()
    #state = models.CharField(max_length = 120)
    material = models.CharField(max_length = 120)
    #Free_volume = models.FloatField()
    container_logo = models.FileField()


    def get_absolute_url(self):
        return reverse('vehicule_app:details', kwargs={'pk' : self.vehicle.pk})


    def __str__(self):
        return self.registration + '-' + self.vehicle.v_type
