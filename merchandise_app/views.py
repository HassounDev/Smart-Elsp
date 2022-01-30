from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from .models import Merchandise, Orderer, LoadUnit, MerchandiseDoc, Product, Tag
from django.utils.translation import ugettext_lazy as _
from django.shortcuts import render, redirect
from .forms import MerchandiseForm, LoadUnitForm, MerchandiseDocForm, TagForm, ProductForm
import pyqrcode

#---------------Merchandise Views------------------

class MerchandiseView(generic.ListView):

    template_name = 'merchandise_app/merchandise.html'
    context_object_name = 'merchandises'

    def get_queryset(self):
        return Merchandise.objects.all()

class DetailView(generic.DetailView):
    model = Merchandise
    template_name = 'merchandise_app/detail.html'

class MerchandiseCreate(CreateView):
    form_class = MerchandiseForm
    template_name = 'merchandise_app/merchandise_form.html'

class MerchandiseUpdate(UpdateView):

    form_class = MerchandiseForm
    template_name = 'merchandise_app/merchandise_form.html'

    def get_queryset(self):
        return Merchandise.objects.all()

class MerchandiseDelete(DeleteView):
    model = Merchandise
    success_url = reverse_lazy('merchandise_app:merchandise')

#---------------LoadUnit Views------------------

class LoadUnitView(generic.ListView):

    template_name = 'merchandise_app/loadunit.html'
    context_object_name = 'loadunits'

    def get_queryset(self):
        return LoadUnit.objects.all()

class LoadUnitCreate(CreateView):
    form_class = LoadUnitForm
    template_name = 'merchandise_app/loadunit_form.html'

class LoadUnitUpdate(UpdateView):
    form_class = LoadUnit
    templae_name = 'merchandise_app/loadunit_form.html'

    def get_queryset(self):
        return LoadUnit.objects.all()

class LoadUnitDelete(DeleteView):
    model = LoadUnit
    success_url = reverse_lazy('merchandise_app:loadunit')

#---------------Orderer Views------------------

class OrdererView(generic.ListView):
    template_name = 'merchandise_app/orderer.html'
    context_object_name = 'orderers'

    def get_queryset(self):
        return Orderer.objects.all()

class OrdererCreate(CreateView):
    model = Orderer
    fields = '__all__'

class OrdererUpdate(UpdateView):
    model = Orderer
    fields = '__all__'

class OrdererDelete(DeleteView):
    model = Orderer
    success_url = reverse_lazy('merchandise_app:orderer')

#---------------Merchandise Doc Views------------------

class MerchandiseDocView(generic.ListView):
    template_name = 'merchandise_app/merchandisedoc.html'
    context_object_name = 'docs'

    def get_queryset(self):
        return MerchandiseDoc.objects.all()

class MerchandiseDocCreate(CreateView):
    form_class = MerchandiseDocForm
    template_name = 'merchandise_app/merchandisedoc_form.html'

class MerchandiseDocUpdate(UpdateView):
    form_class = MerchandiseDocForm
    template_name = 'merchandise_app/merchandisedoc_form.html'

    def get_queryset(self):
        return MerchandiseDoc.objects.all()

class MerchandiseDocDelete(DeleteView):
    model = MerchandiseDoc
    success_url = reverse_lazy('merchandise_app:doc')

#---------------Product Views------------------

class ProductView(generic.ListView):
    template_name = 'merchandise_app/product.html'
    context_object_name = 'products'

    def get_queryset(self):
        return Product.objects.all()

class ProductCreate(CreateView):
    form_class = ProductForm
    template_name = 'merchandise_app/product_form.html'

class ProductUpdate(UpdateView):
    form_class = ProductForm
    template_name = 'merchandise_app/product_form.html'
    def get_queryset(self):
        return Product.objects.all()


class ProductDelete(DeleteView):
    model = Product
    success_url = reverse_lazy('merchandise_app:product')

#---------------Tag Views------------------

class TagView(generic.ListView):
    template_name = 'merchandise_app/tag.html'
    context_object_name = 'tags'

    def get_queryset(self):
        return Tag.objects.all()

class TagCreate(CreateView):
    form_class = TagForm
    template_name = 'merchandise_app/tag_form.html'

class TagUpdate(UpdateView):
    form_class = TagForm
    template_name = 'merchandise_app/tag_form.html'
    def get_queryset(self):
        return Tag.objects.all()

class TagDelete(DeleteView):
    model = Tag
    success_url = reverse_lazy('merchandise_app:tag')
