from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.views.decorators.cache import cache_page
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import View
from .models import Position, Member, Service, Link, Point, Coordonne,CoordNum,PerContact, Location
from merchandise_app.models import Merchandise
from .forms import CordForm, DigCordForm, PerContactForm, PositionForm
from django.shortcuts import render, get_object_or_404
from .services import get_coordonnes_with_cache as get_coordonnes
from .services import get_positions_with_cache as get_positions

CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)


@cache_page(CACHE_TTL)
def coordonnes_view(request):
    return render(request, 'position_app/coordonne_cach.html', {
        'coordonnes': get_coordonnes()
    })

@cache_page(CACHE_TTL)
def positions_view(request):
    return render(request, 'position_app/position_cach.html', {
        'locations': get_positions()
    })


class IndexView(generic.ListView):
    template_name = 'position_app/index.html'
    context_object_name = 'all_position'
    model = Position.objects.all()
    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context.update({
            'locations': Location.nodes.all(),
        })
        return context
    def get_queryset(self):
        return Position.objects.all()

class MemberView(generic.ListView):
    template_name = 'position_app/member.html'
    context_object_name = 'all_member'
    def get_queryset(self):
        return Member.objects.all()
#ddddddddddd
class Showv(generic.ListView):
    template_name = 'position_app/show.html'
    context_object_name = 'merchandises'
    def get_queryset(self):
        return Merchandise.objects.all()


class ServiceView(generic.ListView):
    template_name = 'position_app/service.html'
    context_object_name = 'all_service'
    def get_queryset(self):
        return Service.objects.all()

class LinkView(generic.ListView):
    template_name = 'position_app/link.html'
    context_object_name = 'all_link'
    def get_queryset(self):
        return Link.objects.all()

class PointView(generic.DetailView):
    template_name = 'position_app/point.html'
    context_object_name = 'all_point'
    def get_queryset(self):
        return Point.objects.all()

class CoordView(generic.ListView):
    template_name = 'position_app/coordonne.html'
    context_object_name = 'all_cord'
    def get_queryset(self):
        return Coordonne.objects.all()

class DetailCord(generic.DetailView):
    model = Coordonne
    template_name = 'position_app/detail.html'

class PositionCreate(CreateView):
    form_class = PositionForm
    template_name = 'position_app/position_form.html'

class MemberCreate(CreateView):
    model = Member
    fields = '__all__'

class ServiceCreate(CreateView):
    model = Service
    fields = '__all__'

class LinkCreate(CreateView):
    model = Link
    fields = '__all__'


class PointCreate(CreateView):
    model = Point
    fields = '__all__'

class CoordCreate(CreateView):
    form_class = CordForm
    template_name = 'position_app/coordonne_form.html'

class CoordNumCreate(CreateView):

    form_class = DigCordForm
    template_name = 'position_app/coordnum_form.html'

class PerContactCreate(CreateView):

    form_class = PerContactForm
    template_name = 'position_app/percontact_form.html'

class PositionDelete(DeleteView):
    model = Position
    success_url = reverse_lazy('position_app:index')

class MemberDelete(DeleteView):
    model = Member
    success_url = reverse_lazy('position_app:member')

class ServiceDelete(DeleteView):
    model = Service
    success_url = reverse_lazy('position_app:service')

class LinkDelete(DeleteView):
    model = Link
    success_url = reverse_lazy('position_app:link')

class CoordDelete(DeleteView):
    model = Coordonne
    success_url = reverse_lazy('position_app:coordonne')

class CoordNumDelete(DeleteView):
    model = CoordNum
    success_url = reverse_lazy('position_app:coordonne')

class PerContactDelete(DeleteView):

    model = PerContact
    success_url = reverse_lazy('position_app:coordonne')


class PositionUpdate(UpdateView):
    form_class = PositionForm
    template_name = 'position_app/position_form.html'
    def get_queryset(self):
        return Position.objects.all()


class MemberUpdate(UpdateView):
    model = Member
    fields = '__all__'

class ServiceUpdate(UpdateView):
    model = Service
    fields = '__all__'

class LinkUpdate(UpdateView):
    model = Link
    fields = '__all__'

class CoordUpdate(UpdateView):
    form_class = CordForm
    template_name = 'position_app/coordonne_form.html'
    def get_queryset(slef):
        return Coordonne.objects.all()

class CoordNumUpdate(UpdateView):

    form_class = DigCordForm
    template_name = 'position_app/coordnum_form.html'
    def get_queryset(slef):
        return CoordNum.objects.all()

class PerContactUpdate(UpdateView):

    form_class = PerContactForm
    template_name = 'position_app/percontact_form.html'
    def get_queryset(slef):
        return PerContact.objects.all()
