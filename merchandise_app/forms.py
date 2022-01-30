from .models import Merchandise, Orderer, LoadUnit, Tag, MerchandiseDoc, Product
from django import forms

class MerchandiseForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(MerchandiseForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control col-md-7 col-xs-12'

    orderer = forms.ModelChoiceField(queryset=Orderer.objects.all(),widget = forms.Select())
    designation = forms.CharField(widget = forms.TextInput())
    description = forms.CharField(widget = forms.Textarea())
    category = forms.CharField(widget = forms.TextInput())
    sub_category = forms.CharField(widget = forms.TextInput())
    state = forms.CharField(widget = forms.TextInput())
    longitude = forms.CharField()
    latitude = forms.CharField()

    #category = forms.ModelChoiceField(queryset=Merchandise.objects.values('category').distinct())
    class Meta:
        model = Merchandise
        fields = '__all__'

class LoadUnitForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(LoadUnitForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control col-md-7 col-xs-12'
    class Meta:
        model = LoadUnit
        fields = '__all__'

class TagForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(TagForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control col-md-7 col-xs-12'
    class Meta:
        model = Tag
        fields = '__all__'

class ProductForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control col-md-7 col-xs-12'
    class Meta:
        model = Product
        fields = '__all__'

class MerchandiseDocForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(MerchandiseDocForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control col-md-7 col-xs-12'
    class Meta:
        model = MerchandiseDoc
        fields = '__all__'
