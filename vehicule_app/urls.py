from django.conf.urls import  url
from . import views
from django.template import loader

app_name = 'vehicule_app'
urlpatterns = [
#welcome
    url(r'^$',views.IndexView.as_view(), name='index'),
    url(r'^container/$',views.ContainerView.as_view(), name='container-view'),

#register
    url(r'^register/$', views.UserFormView.as_view(), name='register'),

#/vihecle id
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name = 'details'),

#vehicule_app/vehicle/add
    url(r'vehicle/add/$', views.VehicleCreate.as_view(), name='vehicle-add'),

#vehicule_app/container/add
    url(r'(?P<pk>[0-9]+)/containeradd/$', views.ContainerCreate.as_view(), name='container-add'),
    url(r'container/add0/$', views.ContainerCreateo.as_view(), name='container-addo'),

#r'^(?P<album_id>[0-9]+)/create_song/$'
#vehicule_app/vehicle/2
    url(r'^vehicle/(?P<pk>[0-9]+)/$',views.VehicleUpdate.as_view(),name='vehicle-update'),

#vehicule_app/vehicle/2/delete
    url( r'^(?P<pk>[0-9]+)/delete/$', views.VehicleDelete.as_view(), name='vehicle-delete'),
#delete container
    url( r'^(?P<vehicle_id>[0-9]+)/deletecontainer/(?P<container_id>[0-9]+)/$', views.ContainerDelete, name='container-delete'),


    url(r'^container/edit/(?P<pk>[0-9]+)/$',views.ContainerUpdate.as_view(),name='container-update'),
    url(r'^container/(?P<pk>[0-9]+)/$',views.ContainerUpdate0.as_view(),name='container-update0'),

]
