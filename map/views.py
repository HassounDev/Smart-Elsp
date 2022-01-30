from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect
from django.views.generic import View
from .models import Map



class IndexView(generic.ListView):
    template_name = 'map/index.html'
    context_object_name = 'all_maps'
    def get_queryset(slef):
        return Map.objects.all()
