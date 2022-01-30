from django.conf.urls import url, include
from . import views

urlpatterns = [
    #/dashboard/login
    #/dashboard/login
    #/dashboard/login
    #/dashboard/login
    #/dashboard/login
    #/dashboard/login
    url(r'^login/$', views.UserFormView.as_view(), name="login"),
    #/dashboard/
    url(r'^$', views.dashboard, name="dashboard"),
    #/dashboard/merchandise/
    url(r'^merchandise/', include('merchandise_app.urls')),
    #/dashboard/warehouse/
    url(r'^warehouse/', include('warehouse_app.urls')),
]
