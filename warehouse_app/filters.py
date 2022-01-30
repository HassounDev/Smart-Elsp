from .models import CellType
import django_filters

class CellTypeFilter(django_filters.FilterSet):
    class Meta:
        model = CellType
        fields = '__all__'
