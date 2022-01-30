from django.contrib import admin

# Register your models here.
from .models import Member
from .models import Position
from .models import Service
from .models import Link
from .models import Point
from .models import Coordonne
from .models import CoordNum
from .models import PerContact

admin.site.register(Member)
admin.site.register(Position)
admin.site.register(Service)
admin.site.register(Link)
admin.site.register(Point)
admin.site.register(Coordonne)
admin.site.register(CoordNum)
admin.site.register(PerContact)
