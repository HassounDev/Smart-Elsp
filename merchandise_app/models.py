from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.urlresolvers import reverse

class Orderer(models.Model):
    # ORDERER CHOICES
    ORDERER_TYPE = (
        ('CHARTER', 'Charter'),
        ('LOADER', 'Loader')
    )

    nickname = models.CharField(max_length = 250)
    designation = models.CharField(max_length = 250)
    orderer_type = models.CharField(max_length = 250, choices = ORDERER_TYPE)

    def get_absolute_url(self):
        return reverse('merchandise_app:orderer')

    def __str__(self):
        return "Orderer: " + self.nickname + " " + self.orderer_type

class Merchandise(models.Model):

    orderer = models.ForeignKey(Orderer, on_delete=models.CASCADE)
    designation = models.CharField(max_length = 250)
    description = models.TextField()
    category = models.CharField(max_length = 250) #choices
    sub_category = models.CharField(max_length = 250) #js
    state = models.CharField(max_length = 250)
    longitude = models.FloatField(null=True)
    latitude = models.FloatField(null=True)

    def get_absolute_url(self):
        return reverse('merchandise_app:merchandise')
        #kwargs={'pk': self}

    def __str__(self):
        return self.designation + " " +  self.orderer.nickname

class LoadUnit(models.Model):

    merchandise = models.ForeignKey(Merchandise, on_delete = models.CASCADE)
    designation = models.CharField(max_length = 250)
    description = models.TextField()
    category = models.CharField(max_length = 400) #choices
    sub_category = models.CharField(max_length = 400) #choices
    number_of_products = models.IntegerField()
    volume = models.FloatField()
    width_lu = models.FloatField()
    length_lu = models.FloatField()
    height_lu = models.FloatField()
    value_lu = models.FloatField()
    state_lu = models.CharField(max_length = 250)
    physical_state = models.CharField(max_length = 250)

    def get_absolute_url(self):
        return reverse('merchandise_app:loadunit')


    def __str__(self):
        return self.designation + " " + self.merchandise.designation

class Tag(models.Model):
    loadunit = models.ForeignKey(LoadUnit, on_delete = models.CASCADE)
    receiver = models.CharField(max_length = 250)
    receiver_adress = models.CharField(max_length = 400)
    is_fragile = models.BooleanField(default = False)

    def __str__(self):
        return self.receiver + " " + self.loadunit.designation

    def get_absolute_url(self):
        return reverse('merchandise_app:tag')

class Product(models.Model):
    loadunit = models.ForeignKey(LoadUnit, on_delete = models.CASCADE)
    designation = models.CharField(max_length = 250)
    price = models.FloatField()
    quanity = models.IntegerField()

    def get_absolute_url(self):
        return reverse('merchandise_app:product')


class MerchandiseDoc(models.Model):
    merchandise = models.ForeignKey(Merchandise, on_delete = models.CASCADE)
    doc_type = models.CharField(max_length = 250)
    designation = models.CharField(max_length = 250)
    copy_num = models.FileField()

    def get_absolute_url(self):
        return reverse('merchandise_app:doc')
