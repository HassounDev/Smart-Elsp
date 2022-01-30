from django.contrib.auth import authenticate, login
from django.views.generic import View
from .models import Vehicle , Container
import django_filters

class UserFilter(django_filters.FilterSet):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', ]
