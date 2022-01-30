from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import View
from .models import Vehicle , Container
from .forms import UserForm, VehicleForm , ContainerForm
from django.shortcuts import render, get_object_or_404




class IndexView(generic.ListView):
    template_name = 'vehicule_app/index.html'
    context_object_name = 'all_vihecle'
    paginate_by = 8
    def get_queryset(slef):
        return Vehicle.objects.all()


class ContainerView(generic.ListView):
    template_name = 'vehicule_app/container.html'
    context_object_name = 'all_containers'
    paginate_by = 9
    def get_queryset(slef):
        return Container.objects.all()


class DetailView(generic.DetailView):
    model = Vehicle
    template_name = 'vehicule_app/detail.html'


class VehicleCreate(CreateView):

    form_class = VehicleForm
    template_name = 'vehicule_app/vehicle_form.html'



class ContainerCreate(CreateView):

    form_class = ContainerForm
    template_name = 'vehicule_app/container_form.html'

    def get_form_kwargs(self):
        kwargs = super(ContainerCreate, self).get_form_kwargs()
        if kwargs['instance'] is None:
            kwargs['instance'] = Container()
            kwargs['instance'].vehicle_id = self.kwargs['pk'] # Fetch the vehicle_id from the URL
        return kwargs

class ContainerCreateo(CreateView):

    form_class = ContainerForm
    template_name = 'vehicule_app/container_form.html'
    success_url = '/vehicule_app/container'


class VehicleUpdate(UpdateView):
    form_class = VehicleForm
    template_name = 'vehicule_app/vehicle_form.html'
    def get_queryset(slef):
        return Vehicle.objects.all()

class ContainerUpdate(UpdateView):
    form_class = ContainerForm
    template_name = 'vehicule_app/vehicle_form.html'
    def get_queryset(slef):
        return Container.objects.all()

class ContainerUpdate0(UpdateView):
    form_class = ContainerForm
    template_name = 'vehicule_app/vehicle_form.html'
    def get_queryset(slef):
        return Container.objects.all()

class VehicleDelete(DeleteView):
    model = Vehicle
    success_url = reverse_lazy('vehicule_app:index')

def ContainerDelete(request, vehicle_id, container_id):
    vehicle = get_object_or_404(Vehicle, pk=vehicle_id)
    container = Container.objects.get(pk=container_id)
    container.delete()
    return render(request, 'vehicule_app/detail.html', {'vehicle': vehicle})

class UserFormView(View):
    form_class = UserForm
    template_name = 'vehicule_app/registration_form.html'

    #display blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    #process from database
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():

            user = form.save(commit = False)

            #cleaned (normalized) data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.save()

            #returns User objects if credentials are correct
            user = authenticate(username=username, password=password)

            if user is not None:

                if user.is_active:

                    login(request, user)
                    return redirect('vehicule_app:index')
        return render(request, self.template_name, {'form': form})
