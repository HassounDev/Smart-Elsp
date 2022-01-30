from django import forms
from .models import Warehouse, Activity, Building, Zone, Radius, Support, Cell, CellType, Parking

class WarehouseForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(WarehouseForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control col-md-7 col-xs-12'
    class Meta:
        model = Warehouse
        fields = '__all__'

class ActivityForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ActivityForm, self).__init__(*args, **kwargs)
        #self.fields['warehouse'].queryset = Warehouse.objects.filter(id=warehouse_id)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control col-md-7 col-xs-12'
    time_p = forms.DateTimeField(widget=forms.TextInput(attrs={'placeholder': 'YYYY-MM-DD hh:mm:ss'}))
    time_r = forms.DateTimeField(widget=forms.TextInput(attrs={'placeholder': 'YYYY-MM-DD hh:mm:ss'}))
    #time_test = forms.DateTimeField(widget=forms.TextInput(attrs={'type': 'date'}))
    class Meta:
        model = Activity
        fields = '__all__'

class BuildingForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(BuildingForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control col-md-7 col-xs-12'
    class Meta:
        model = Building
        fields = '__all__'

class ZoneForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ZoneForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control col-md-7 col-xs-12'
    class Meta:
        model = Zone
        fields = '__all__'

class RadiusForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(RadiusForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control col-md-7 col-xs-12'
    class Meta:
        model = Radius
        fields = '__all__'

class SupportForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(SupportForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control col-md-7 col-xs-12'
    class Meta:
        model = Support
        fields = '__all__'

class CellForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CellForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control col-md-7 col-xs-12'
    class Meta:
        model = Cell
        fields = '__all__'

class CellTypeForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CellTypeForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control col-md-7 col-xs-12'
    class Meta:
        model = CellType
        fields = '__all__'

class ParkingForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ParkingForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control col-md-7 col-xs-12'

    state_p = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class':'js-switch'}))
    class Meta:
        model = Parking
        fields = '__all__'
