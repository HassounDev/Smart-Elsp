from django.db import models
from django.core.urlresolvers import reverse
from django_neomodel import DjangoNode
from neomodel import FloatProperty,StructuredNode, StringProperty, DateTimeProperty, UniqueIdProperty, Relationship, RelationshipTo, StructuredRel

# Create your models here.

class Member(models.Model):

    TYPE_MEMBER = (('LOADER','Loader'),('WAREHOUSEMAN','Warehouseman'),
                  ('TRANSPORTER','Transporter'))
    m_type = models.CharField(max_length = 250 , choices = TYPE_MEMBER)
    adress = models.CharField(max_length = 250)
    tele   = models.CharField(max_length = 250)
    email  = models.EmailField()
    fax    = models.CharField(max_length = 250)

    def get_absolute_url(self):
        return reverse('position_app:member')

    def __str__(self):
        return self.m_type + '-' + self.email

class Location(DjangoNode):
    name = StringProperty()
    lat = FloatProperty()
    lng = FloatProperty()
    road_to = Relationship('Position','ROAD_TO')
    class Meta:
        app_label = 'roads'

class Position(models.Model):

    FONCTION = (('GARAGE','Garage'),('RESRT AREA','Rest Area'),('PAYING','Paying'),('PARK','Park'),
               ('CUSTOMS','Customs'),('OTHERS','Others'))
    ref = models.CharField(max_length = 250)
    function = models.CharField(max_length = 250 , choices = FONCTION)
    longitude = models.FloatField()
    latitude = models.FloatField()
    member= models.ForeignKey(Member, on_delete= models.CASCADE)

    def get_absolute_url(self):
        return reverse('position_app:index')

    def __str__(self):
        return self.ref + '-' + self.member.m_type


class Service(models.Model):

    TYPE_SERVICE = (('LOADING','Loading'),('UNLOADING','Unloading'))
    s_type = models.CharField(max_length = 250 , choices = TYPE_SERVICE)
    label = models.CharField(max_length = 250)
    value = models.CharField(max_length = 250)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('position_app:service')

    def __str__(self):
        return self.s_type +'-'+ self.position


class Link(models.Model):

    ref = models.CharField(max_length = 250)
    distance = models.FloatField()
    time = models.FloatField()#durationField()
    rate = models.FloatField()
    type_road = models.CharField(max_length = 250)#choices
    starting_position = models.ForeignKey(Position,related_name="starting_position_set", on_delete = models.CASCADE)
    arrival_position = models.ForeignKey(Position, related_name="arrival_position_set", on_delete = models.CASCADE)

    def get_absolute_url(self):
        return reverse('position_app:link')

    def __str__(self):
        return self.ref + '-' + self.starting_position.ref + '-' + self.arrival_position.ref

class Point(models.Model):

    FONCTION = (('GARAGE','Garage'),('BILLING','Billing'),('DELIVERY','Delivery'),('LOADING','Loading'),
               ('UNLOADING','Ubloading'))
    ref = models.CharField(max_length = 250)
    function = models.CharField(max_length = 250 , choices = FONCTION)
    longitude = models.FloatField()
    latitude = models.FloatField()
    link = models.ForeignKey(Link, on_delete = models.CASCADE)

    def get_absolute_url(self):
        return reverse('position_app:point')

    def __str__(self):
        return self.fonction + '-' + self.link.ref

class Coordonne(models.Model):

    ref = models.CharField(max_length = 250)
    NATURE = (('SEAT','Seat'),('RESRT AREA','Rest Area'),('PAYING','Paying'),('PARK','Park'),
               ('CUSTOMS','Customs'),('OTHERS','Others'))

    nature = models.CharField(max_length = 250 , choices= NATURE)
    adresse = models.TextField()
    country = models.CharField(max_length = 250)
    city = models.CharField(max_length = 250)
    area = models.CharField(max_length = 250)
    postal_code = models.IntegerField()
    longitude = models.FloatField()
    latitude = models.FloatField()

    def get_absolute_url(self):
        return reverse('position_app:coordonne')

    def __str__(self):
        return self.ref + '-' + self.nature


class CoordNum(models.Model):

    ref = models.CharField(max_length = 250)
    cor_type = models.CharField(max_length = 250 )
    value = models.CharField(max_length = 250)
    coordonne = models.ForeignKey(Coordonne, on_delete = models.CASCADE)

    def get_absolute_url(self):
        return reverse('position_app:detail-cord',kwargs={'pk' : self.coordonne.pk})


    def __str__(self):
        return self.ref + '-' + self.coordonne.nature

class PerContact(models.Model):

    salutation = models.CharField( max_length = 250 )
    nom = models.CharField( max_length = 250 )
    fonction = models.CharField( max_length = 250 )
    telefixe = models.CharField( max_length = 250 )
    telegsm = models.CharField( max_length = 250 )
    email = models.EmailField()
    coordonne = models.ForeignKey(Coordonne, on_delete = models.CASCADE)

    def get_absolute_url(self):
        return reverse('position_app:detail-cord',kwargs={'pk' : self.coordonne.pk})


    def __str__(self):
        return self.ref + '-' + self.coordonne.nature
