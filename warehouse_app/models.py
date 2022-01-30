from django.db import models
from django.core.urlresolvers import reverse
# Create your models here.
class Warehouse(models.Model):
    KIND =(
        ('1','Entrepôt public'),
        ('2','Entrepôt privé'),
        ('3','Entrepôt ouvert'),
        ('4','Entrepôt fermés'),
        ('5','Entrepôt semi-ouverts'),
        ('6','Entrepôt A'),
        ('7','Entrepôt B'),
        ('8','Entrepôt C'),
        ('9','Entrepôt d\'usine'),
        ('10','Entrepôt central'),
        ('11','Entrepôt distribution'),
        ('12','Entrepôt détaillant'),
        ('13','Entrepôt particulier - Messagerie'),
        ('14','Entrepôt particulier - Frigorifique'),
        ('15','Entrepôt particulier - Pharmaceutique')
    )
    name = models.CharField(max_length = 250)
    type_entrepot = models.CharField(max_length=250, choices = KIND)
    is_available = models.BooleanField(default = False) #state
    number_building = models.IntegerField()
    description = models.TextField()
    wh_pic = models.FileField()


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('warehouse_app:warehouse')

class Activity(models.Model):

    ACTION =(
        ('LOADING','Loading'),
        ('UNLOADING','Unloading')
    )

    activity_type = models.CharField(max_length=250, choices = ACTION)
    designation = models.CharField(max_length=250)
    time_p = models.DateTimeField() # FALSE
    time_r = models.DateTimeField()
    state_activity = models.CharField(max_length = 400)
    warehouse = models.ForeignKey(Warehouse, on_delete = models.CASCADE)
    # DurationField (-)

    def __str__(self):
        return self.activity_type + " : " + self.warehouse.name

    def get_absolute_url(self):
        return reverse('warehouse_app:activity')


class Building(models.Model):

    name = models.CharField(max_length = 250)
    humidity = models.FloatField()
    temperature = models.FloatField()
    volume = models.FloatField()
    number_zone = models.IntegerField()
    warehouse = models.ForeignKey(Warehouse, on_delete = models.CASCADE)

    def __str__(self):
        return self.name + self.warehouse.name

    def get_absolute_url(self):
        return reverse('warehouse_app:building')

class Zone(models.Model):

    name = models.CharField(max_length = 250)
    number_location = models.IntegerField()
    volume = models.FloatField()
    total_surface = models.FloatField()
    usable_surface = models.FloatField()
    building = models.ForeignKey(Building, on_delete = models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('warehouse_app:zone')


class Radius(models.Model):

    number = models.IntegerField()
    length = models.FloatField()
    width = models.FloatField()
    height = models.FloatField()
    number_floor = models.IntegerField()
    number_cell = models.IntegerField()
    zone = models.ForeignKey(Zone, on_delete = models.CASCADE)

    def __str__(self):
        return "Radius N: " + str(self.number) + " " + str(self.zone.name)

    def get_absolute_url(self):
        return reverse('warehouse_app:radius')


class Support(models.Model):

    last_name = models.CharField(max_length = 250)
    first_name = models.CharField(max_length = 250)
    phone = models.BigIntegerField()
    email = models.EmailField(max_length=254)
    fax = models.CharField(max_length = 400)
    zone = models.ForeignKey(Zone, on_delete = models.CASCADE)

    def __str__(self):
        return "Support: " + self.last_name + " " + self.first_name

    def get_absolute_url(self):
        return reverse('warehouse_app:support')

class Cell(models.Model):

    cell_type = models.CharField(max_length = 254)
    surface_available = models.FloatField()
    volume_available = models.FloatField()
    weight_available = models.FloatField()
    radius = models.ForeignKey(Radius, on_delete = models.CASCADE)

    def __str__(self):
        return self.cell_type + "Radius N: " + self.radius.number

    def get_absolute_url(self):
        return reverse('warehouse_app:cell')

class CellType(models.Model):

    line_number = models.IntegerField()
    cell_surface = models.FloatField()
    cell_volume = models.FloatField()
    max_weight_cell = models.FloatField()
    radius = models.ForeignKey(Radius, on_delete = models.CASCADE)

    def __str__(self):
        return "cell type number: " + self.line_number

    def get_absolute_url(self):
        return reverse('warehouse_app:celltype')

class Parking(models.Model):

    number = models.IntegerField()
    name = models.CharField(max_length = 250)
    type_p = models.CharField(max_length = 250)
    surface_p = models.FloatField()
    number_places = models.IntegerField()
    available_places = models.IntegerField()
    state_p = models.BooleanField(default = False)
    warehouse = models.ForeignKey(Warehouse, on_delete = models.CASCADE)

    def __str__(self):
        return self.name + " " + self.warehouse.name

    def get_absolute_url(self):
        return reverse('warehouse_app:parking')
