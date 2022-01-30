from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from .models import Warehouse, Activity, Building, Zone, Radius, Support, Cell, CellType, Parking
from django.utils.translation import ugettext_lazy as _
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from .forms import WarehouseForm, ActivityForm, ZoneForm, BuildingForm, CellForm, CellTypeForm, ParkingForm, RadiusForm, SupportForm
from django.contrib import messages
from .filters import CellTypeFilter
#---------------Warehouse Views------------------

class WarehouseView(generic.ListView):
    paginate_by = 15
    template_name = 'warehouse_app/warehouse.html'
    context_object_name = 'warehouses'

    def get_queryset(self):
        return Warehouse.objects.all()

class DetailView(generic.DetailView):
    model = Warehouse
    form_class = WarehouseForm
    template_name = 'warehouse_app/detail.html'

class WarehouseCreate(CreateView):
    form_class = WarehouseForm
    template_name = 'warehouse_app/warehouse_form.html'


class WarehouseUpdate(UpdateView):
    form_class = WarehouseForm
    template_name = 'warehouse_app/warehouse_form.html'

    def get_queryset(self):
        return Warehouse.objects.all()

class WarehouseDelete(DeleteView):
    model = Warehouse
    success_url = reverse_lazy('warehouse_app:warehouse')

#---------------Activity Views------------------

class ActivityView(generic.ListView):
    paginate_by = 12
    template_name = 'warehouse_app/activity.html'
    context_object_name = 'activities'

    def get_queryset(self):
        return Activity.objects.all()


class ActivityCreate(CreateView):
    form_class = ActivityForm
    template_name = 'warehouse_app/activity_form.html'

class ActivityUpdate(UpdateView):
    form_class = ActivityForm
    template_name = 'warehouse_app/activity_form.html'
    #form = ActivityForm()
    #form.fields['warehouse'].queryset = Warehouse.objects.filter(id)

    def get_queryset(self):
        return Activity.objects.all()

class ActivityDelete(DeleteView):
    model = Activity
    success_url = reverse_lazy('warehouse_app:activity')

#---------------Building Views------------------

class BuildingView(generic.ListView):
    paginate_by = 12
    template_name = 'warehouse_app/building.html'
    context_object_name = 'buildings'

    def get_queryset(self):
        return Building.objects.all()


class BuildingCreate(CreateView):
    form_class = BuildingForm
    template_name = 'warehouse_app/building_form.html'

class BuildingUpdate(UpdateView):
    form_class = BuildingForm
    template_name = 'warehouse_app/building_form.html'

    def get_queryset(self):
        return Building.objects.all()

class BuildingDelete(DeleteView):
    model = Building
    success_url = reverse_lazy('warehouse_app:building')

#---------------Zone Views------------------

class ZoneView(generic.ListView):
    paginate_by = 12
    template_name = 'warehouse_app/zone.html'
    context_object_name = 'zones'

    def get_queryset(self):
        return Zone.objects.all()


class ZoneCreate(CreateView):
    form_class = ZoneForm
    template_name = 'warehouse_app/zone_form.html'

class ZoneUpdate(UpdateView):
    form_class = ZoneForm
    template_name = 'warehouse_app/zone_form.html'

    def get_queryset(self):
        return Zone.objects.all()

class ZoneDelete(DeleteView):
    model = Zone
    success_url = reverse_lazy('warehouse_app:zone')

#---------------Radius Views------------------

class RadiusView(generic.ListView):
    paginate_by = 12
    template_name = 'warehouse_app/radius.html'
    context_object_name = 'all_radius'

    def get_queryset(self):
        return Radius.objects.all()


class RadiusCreate(CreateView):
    form_class = RadiusForm
    template_name = 'warehouse_app/radius_form.html'

class RadiusUpdate(UpdateView):
    form_class = RadiusForm
    template_name = 'warehouse_app/radius_form.html'

    def get_queryset(self):
        return Radius.objects.all()

class RadiusDelete(DeleteView):
    model = Radius
    success_url = reverse_lazy('warehouse_app:radius')

#---------------Support Views------------------

class SupportView(generic.ListView):
    paginate_by = 12
    template_name = 'warehouse_app/support.html'
    context_object_name = 'supports'

    def get_queryset(self):
        return Support.objects.all()


class SupportCreate(CreateView):
    form_class = SupportForm
    template_name = 'warehouse_app/support_form.html'

class SupportUpdate(UpdateView):
    form_class = SupportForm
    template_name = 'warehouse_app/support_form.html'

    def get_queryset(self):
        return Support.objects.all()

class SupportDelete(DeleteView):
    model = Support
    success_url = reverse_lazy('warehouse_app:support')

#---------------Cell Views------------------

class CellView(generic.ListView):
    paginate_by = 12
    template_name = 'warehouse_app/cell.html'
    context_object_name = 'cells'

    def get_queryset(self):
        return Cell.objects.all()


class CellCreate(CreateView):
    form_class = CellForm
    template_name = 'warehouse_app/cell_form.html'

class CellUpdate(UpdateView):
    form_class = CellForm
    template_name = 'warehouse_app/cell_form.html'

    def get_queryset(self):
        return Cell.objects.all()

class CellDelete(DeleteView):
    model = Cell
    success_url = reverse_lazy('warehouse_app:cell')

#---------------Celltype Views------------------
def search(request):
    celltype_list = CellType.objects.all()
    celltype_filter = CellTypeFilter(request.GET, queryset = celltype_list)
    return render(request, 'celltype_list.html', {'filter': celltype_filter})




class CellTypeView(generic.ListView):
    #paginate_by = 12
    template_name = 'warehouse_app/celltype.html'
    context_object_name = 'celltypes'

    def get_queryset(self):
        return CellType.objects.all()


class CellTypeCreate(CreateView):
    form_class = CellTypeForm
    template_name = 'warehouse_app/celltype_form.html'

def celltype_create(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = CellTypeForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            #Message Success :
            messages.success(request,"Successfuly Created", extra_tags="success_message")
            # redirect to a new URL:
            return HttpResponseRedirect(instance.get_absolute_url())
        else:
            messages.error(request,"Failed",extra_tags="fail_message")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = CellTypeForm()

    return render(request, 'celltype_create.html', {'form': form})

# ------------------------------Class View - Update
class CellTypeUpdate(UpdateView):
    form_class = CellTypeForm
    template_name = 'warehouse_app/celltype_form.html'

    def get_queryset(self):
        return CellType.objects.all()
# ------------------------------Function View - Update
def celltype_update(request, pk):
    instance = get_object_or_404(CellType, id=pk)

    form = CellTypeForm(request.POST or None, instance = instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())


    return render(request, 'celltype_create.html', {'form': form})

class CellTypeDelete(DeleteView):
    model = CellType
    success_url = reverse_lazy('warehouse_app:celltype')

#---------------Parking Views------------------

class ParkingView(generic.ListView):
    paginate_by = 12
    template_name = 'warehouse_app/parking.html'
    context_object_name = 'parking'

    def get_queryset(self):
        return Parking.objects.all()


class ParkingCreate(CreateView):
    form_class = ParkingForm
    template_name = 'warehouse_app/parking_form.html'

class ParkingUpdate(UpdateView):
    form_class = ParkingForm
    template_name = 'warehouse_app/parking_form.html'

    def get_queryset(self):
        return Parking.objects.all()

class ParkingDelete(DeleteView):
    model = Parking
    success_url = reverse_lazy('warehouse_app:parking')
