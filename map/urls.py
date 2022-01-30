from django.conf.urls import  url
from . import views
from django.template import loader

app_name = 'map'
urlpatterns = [
#welcome
    url(r'^$',views.IndexView.as_view(), name='index'),
#register
#    url(r'^register/$', views.UserFormView.as_view(), name='register'),


]
