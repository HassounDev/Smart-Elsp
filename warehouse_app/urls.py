from django.conf.urls import url
from . import views

app_name = 'warehouse_app'

urlpatterns = [

    #--------------warehouse URLS :

    # /dashboard/warehouse/
    url(r'^$', views.WarehouseView.as_view(), name='warehouse'),
    url(r'^search/$', views.search, name='search'),

    # /dashboard/warehouse/1[id]
    url(r'^(?P<pk>[0-9]+)$', views.DetailView.as_view(), name='detail'),

    # /dashboard/warehouse/add_wh/
    url(r'^add_wh/', views.WarehouseCreate.as_view(), name="warehouse-add"),

    #  /dashboard/warehouse/update_wh/1/
    url(r'^update_wh/(?P<pk>[0-9]+)/$', views.WarehouseUpdate.as_view(), name="warehouse-update"),

    # /dashboard/warehouse/[id]/delete_wh/
    url(r'^(?P<pk>[0-9]+)/delete_wh/$', views.WarehouseDelete.as_view(), name="warehouse-delete"),

    #--------------Activity URLS :

    # /dashboard/warehouse/activity
    url(r'^activity$', views.ActivityView.as_view(), name='activity'),

    # /dashboard/warehouse/add_activity/
    url(r'^add_activity/', views.ActivityCreate.as_view(), name="activity-add"),

    #  /dashboard/warehouse/update_wh/1/
    url(r'^update_activity/(?P<pk>[0-9]+)/$', views.ActivityUpdate.as_view(), name="activity-update"),

    # /dashboard/warehouse/[id]/delete_activity/
    url(r'^(?P<pk>[0-9]+)/delete_activity/$', views.ActivityDelete.as_view(), name="activity-delete"),

    #--------------Building URLS :

    # /dashboard/warehouse/building
    url(r'^building$', views.BuildingView.as_view(), name='building'),

    # /dashboard/warehouse/add_building/
    url(r'^add_building/', views.BuildingCreate.as_view(), name="building-add"),

    #  /dashboard/warehouse/update_building/1/
    url(r'^update_building/(?P<pk>[0-9]+)/$', views.BuildingUpdate.as_view(), name="building-update"),

    # /dashboard/warehouse/[id]/delete_building/
    url(r'^(?P<pk>[0-9]+)/delete_building/$', views.BuildingDelete.as_view(), name="building-delete"),

    #--------------Zone URLS :

    # /dashboard/warehouse/zone
    url(r'^zone$', views.ZoneView.as_view(), name='zone'),

    # /dashboard/warehouse/add_zone/
    url(r'^add_zone/', views.ZoneCreate.as_view(), name="zone-add"),

    #  /dashboard/warehouse/update_zone/1/
    url(r'^update_zone/(?P<pk>[0-9]+)/$', views.ZoneUpdate.as_view(), name="zone-update"),

    # /dashboard/warehouse/[id]/delete_zone/
    url(r'^(?P<pk>[0-9]+)/delete_zone/$', views.ZoneDelete.as_view(), name="zone-delete"),

    #--------------Radius URLS :

    # /dashboard/warehouse/radius
    url(r'^radius$', views.RadiusView.as_view(), name='radius'),

    # /dashboard/warehouse/add_radius/
    url(r'^add_radius/', views.RadiusCreate.as_view(), name="radius-add"),

    #  /dashboard/warehouse/update_radius/1/
    url(r'^update_radius/(?P<pk>[0-9]+)/$', views.RadiusUpdate.as_view(), name="radius-update"),

    # /dashboard/warehouse/[id]/delete_radius/
    url(r'^(?P<pk>[0-9]+)/delete_radius/$', views.RadiusDelete.as_view(), name="radius-delete"),

    #--------------Support URLS :

    # /dashboard/warehouse/support
    url(r'^support$', views.SupportView.as_view(), name='support'),

    # /dashboard/warehouse/add_support/
    url(r'^add_support/', views.SupportCreate.as_view(), name="support-add"),

    #  /dashboard/warehouse/update_support/1/
    url(r'^update_support/(?P<pk>[0-9]+)/$', views.SupportUpdate.as_view(), name="support-update"),

    # /dashboard/warehouse/[id]/delete_support/
    url(r'^(?P<pk>[0-9]+)/delete_support/$', views.SupportDelete.as_view(), name="support-delete"),

    #--------------Cell URLS :

    # /dashboard/warehouse/cell
    url(r'^cell$', views.CellView.as_view(), name='cell'),

    # /dashboard/warehouse/add_cell/
    url(r'^add_cell/', views.CellCreate.as_view(), name="cell-add"),

    #  /dashboard/warehouse/update_cell/1/
    url(r'^update_cell/(?P<pk>[0-9]+)/$', views.CellUpdate.as_view(), name="cell-update"),

    # /dashboard/warehouse/[id]/delete_cell/
    url(r'^(?P<pk>[0-9]+)/delete_cell/$', views.CellDelete.as_view(), name="cell-delete"),

    #--------------CellType URLS :

    # /dashboard/warehouse/celltype
    url(r'^celltype$', views.CellTypeView.as_view(), name='celltype'),

    # /dashboard/warehouse/add_celltype/
    url(r'^add_celltype/', views.CellTypeCreate.as_view(), name="celltype-add"),
    #url(r'^add_celltype/', views.celltype_create, name='celltype-add'),

    #  /dashboard/warehouse/update_celltype/1/
    url(r'^update_celltype/(?P<pk>[0-9]+)/$', views.CellTypeUpdate.as_view(), name="celltype-update"),
    #url(r'^update_celltype/(?P<pk>\d+)/$', views.celltype_update, name="celltype-update"),

    # /dashboard/warehouse/[id]/delete_celltype/
    url(r'^(?P<pk>[0-9]+)/delete_celltype/$', views.CellTypeDelete.as_view(), name="celltype-delete"),

    #--------------Parking URLS :

    # /dashboard/warehouse/parking
    url(r'^parking$', views.ParkingView.as_view(), name='parking'),

    # /dashboard/warehouse/add_parking/
    url(r'^add_parking/', views.ParkingCreate.as_view(), name="parking-add"),

    #  /dashboard/warehouse/update_parking/1/
    url(r'^update_parking/(?P<pk>[0-9]+)/$', views.ParkingUpdate.as_view(), name="parking-update"),

    # /dashboard/warehouse/[id]/delete_parking/
    url(r'^(?P<pk>[0-9]+)/delete_parking/$', views.ParkingDelete.as_view(), name="parking-delete"),


]
