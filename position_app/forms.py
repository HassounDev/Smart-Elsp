from django.contrib.auth.models import User
from django import forms
from .models import Coordonne, CoordNum, PerContact, Position

NATURE = (('SEAT','Seat'),('RESRT AREA','Rest Area'),('PAYING','Paying'),('PARK','Park'),
           ('CUSTOMS','Customs'),('OTHERS','Others'))


class CordForm(forms.ModelForm):

    ref = forms.CharField()
    nature = forms.ChoiceField( choices=NATURE , widget=forms.Select(attrs={'class':'form-control'}))
    adresse = forms.CharField()
    country = forms.CharField()
    city = forms.CharField()
    area = forms.CharField()
    postal_code = forms.CharField()
    longitude = forms.CharField(widget=forms.TextInput(attrs = {'onfocus' : "document.getElementById('map').style.display = 'block' ;",'onblur' : "document.getElementById('map').style.display = 'none' ;", }))
    latitude = forms.CharField(widget=forms.TextInput(attrs = {'onfocus' : "document.getElementById('map').style.display = 'block' ;",'onblur' : "document.getElementById('map').style.display = 'none' ;", }))

    def __init__(self, *args, **kwargs):
        super(CordForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Coordonne
        fields = '__all__'

class DigCordForm(forms.ModelForm):

    ref = forms.CharField()
    cor_type = forms.CharField()
    value = forms.CharField()
    coordonne = forms.ModelChoiceField(queryset=Coordonne.objects.all(),widget=forms.Select(attrs={'class':'form-control'}))

    def __init__(self, *args, **kwargs):
        super(DigCordForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = CoordNum
        fields = '__all__'

class PerContactForm(forms.ModelForm):

    salutation = forms.CharField()
    nom =forms.CharField()
    fonction = forms.CharField()
    telefixe =forms.CharField()
    telegsm = forms.CharField()
    email = forms.EmailField()
    coordonne = forms.ModelChoiceField(queryset=Coordonne.objects.all(),widget=forms.Select(attrs={'class':'form-control'}))

    def __init__(self, *args, **kwargs):
        super(PerContactForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = PerContact
        fields = '__all__'

class PositionForm(forms.ModelForm):

        def __init__(self, *args, **kwargs):
            super(PositionForm, self).__init__(*args, **kwargs)
            for field_name, field in self.fields.items():
                field.widget.attrs['class'] = 'form-control'

        class Meta:
            model = Position
            fields = '__all__'
