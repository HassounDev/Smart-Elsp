from django.contrib.auth.models import User
from django import forms
from .models import Vehicle, Container
from position_app.models import Member

VEHICLE_TYPE = (('------','----'),('CAR','Car'),('TRUCK','Truck'),('VAN','Van'))
VEHICLE_SOUS_TYPE = (('------','----'),('CAR1','Car1'),('TRUCK1','Truck1'),('VAN1','Van1'))

CONTAINER_TYPE = (('------','----'),('Dry Conteneurs','Dry Conteneurs'),('Double Door Containers','Double Door Containers'),('Flat rack container','Flat rack container'),('Open top container','Open top container'),('Containers with lateral opening'
,'Containers with lateral opening'),('Refrigerated container','Refrigerated containers'),('Isothermal container','Isothermal container'),('Tank container','Tank container'))
CONTAINER_SOUS_TYPE = (('------','----'),('Standard 20’ dry','Standard 20’ dry'),('Standard 20 HC','Standard 20 HC'),('Standard 40’ dry','Standard 40’ dry'),('Standard 40’ HC','Standard 40’ HC'),('Standard 40’ HC','Standard 40’ HC'),('Standard 20','Standard 20'),('Standard 40','Standard 40'),('Standard 40','Standard 40')
,('taille 20’','taille 20’'),('taille 40’','taille 40’'))

class UserForm(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username','email','password']

class VehicleForm(forms.ModelForm):

    member = forms.ModelChoiceField(required=False,queryset=Member.objects.filter(m_type='TRANSPORTER'),widget=forms.Select(attrs={'class':'form-control'}))
    current_registration = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'current registration'}))
    n_insurance = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'n insurance'}))
    mark = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Mark'}))
    v_type = forms.ChoiceField( choices=VEHICLE_TYPE,widget=forms.Select(attrs={'class':'form-control'}))
    v_sub_type = forms.ChoiceField(choices=VEHICLE_SOUS_TYPE,widget=forms.Select(attrs={'class':'form-control'}))
    v_place_nbr = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'v place nbr'}))
    v_average_consumption_city = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'v average consumption city'}))
    v_average_consumption_road = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'v average consumption road'}))
    physical_state = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'physical state'}))
    mileage = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'mileage'}))

    def __init__(self, *args, **kwargs):
        super(VehicleForm, self).__init__(*args, **kwargs)

        self.fields['member'].label = 'transporter'
        self.fields['v_average_consumption_city'].label = 'consumption city'
        self.fields['v_average_consumption_road'].label = 'consumption road'


    class Meta:
        model = Vehicle
        fields = '__all__'

class ContainerForm(forms.ModelForm):
    #filter(id = vehicle.id)
    #vehicle = forms.ModelChoiceField(required=False,queryset=Vehicle.objects.all(),widget=forms.Select(attrs={'class':'form-control'}))
    container_ref =  forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'ref'}))
    registration = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':' registration'}))
    container_type = forms.ChoiceField( choices=CONTAINER_TYPE,widget=forms.Select(attrs={'class':'form-control'}))
    container_sub_type = forms.ChoiceField(choices=CONTAINER_SOUS_TYPE,widget=forms.Select(attrs={'class':'form-control'}))
    volume = forms.FloatField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'volume'}))
    height_ex = forms.FloatField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'external height'}))
    width_ex = forms.FloatField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'external width'}))
    length_ex = forms.FloatField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'external legth'}))
    height_in = forms.FloatField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'internal height'}))
    width_in = forms.FloatField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'internal width'}))
    length_in = forms.FloatField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'internal legth'}))
    #free_surface = forms.FloatField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'free surface'}))
    weight = forms.FloatField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'weight'}))
    capacity = forms.FloatField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'capacity'}))
    function = forms.CharField(widget = forms.Textarea())
    material = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':' material'}))
    #weight_max = forms.FloatField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'weight max'}))
    #state = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'state'}))
    #Free_volume = forms.FloatField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'free volume'}))

    def __init__(self, *args, **kwargs):
        #vehicle_id = kwargs.pop('vehicle_id',None)
        super(ContainerForm, self).__init__(*args, **kwargs)
        #if vehicle_id:
            #self.fields['vehicle'].queryset = Vehicle.objects.filter(id=vehicle_id)

    class Meta:
        model = Container
        fields = '__all__'
        exclude = ['vehicle']
