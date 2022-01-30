from django.conf.urls import url
from . import views

app_name = 'merchandise_app'

urlpatterns = [
    #--------------Merchandise URLS :

    # /dashboard/merchandise/merch/
    url(r'^merch/$', views.MerchandiseView.as_view(), name='merchandise'),

    # /dashboard/merchandise/1[id]
    url(r'^(?P<pk>[0-9]+)$', views.DetailView.as_view(), name='detail'),

    # /dashboard/merchandise/add_m/
    url(r'^add_m/', views.MerchandiseCreate.as_view(), name="merch-add"),

    #  /dashboard/merchandise/update_m/1/
    url(r'^update_m/(?P<pk>[0-9]+)/$', views.MerchandiseUpdate.as_view(), name="merch-update"),

    # /dashboard/merchandise/[id]/delete/
    url(r'^(?P<pk>[0-9]+)/delete_merch/$', views.MerchandiseDelete.as_view(), name="merch-delete"),

    #--------------Orderer URLS :

    # /dashboard/merchandise/orderer/
    url(r'^orderer/', views.OrdererView.as_view(), name='orderer'),

    #/dashboard/merchandise/add_o/
    url(r'^add_o/', views.OrdererCreate.as_view(), name="orderer-add"),

    #/dashboard/merchandise/update_o/
    url(r'^update_o/(?P<pk>[0-9]+)/$', views.OrdererUpdate.as_view(), name="orderer-update"),

    #/dashboard/merchandise/[id]/delete_o
    url(r'^(?P<pk>[0-9]+)/delete_o/$', views.OrdererDelete.as_view(), name="orderer-delete"),


    #--------------LoadUnit URLS :


    url(r'^loadunit/$', views.LoadUnitView.as_view(), name='loadunit'),

    url(r'^add_lu/', views.LoadUnitCreate.as_view(), name="lu-add"),

    url(r'^update_lu/(?P<pk>[0-9]+)/$', views.LoadUnitUpdate.as_view(), name="lu-update"),

    url(r'^(?P<pk>[0-9]+)/delete_lu/$', views.LoadUnitDelete.as_view(), name="lu-delete"),

    #--------------Merchandise Docs URLS :

    # /dashboard/merchandise/doc/
    url(r'^doc/', views.MerchandiseDocView.as_view(), name='doc'),

    #/dashboard/merchandise/add_doc/
    url(r'^add_doc/', views.MerchandiseDocCreate.as_view(), name="doc-add"),

    #/dashboard/merchandise/update_doc/
    url(r'^update_doc/(?P<pk>[0-9]+)/$', views.MerchandiseDocUpdate.as_view(), name="doc-update"),

    #/dashboard/merchandise/[id]/delete_doc
    url(r'^(?P<pk>[0-9]+)/delete_doc/$', views.MerchandiseDocDelete.as_view(), name="doc-delete"),

    #--------------Products URLS :

    # /dashboard/merchandise/product/
    url(r'^product/', views.ProductView.as_view(), name='product'),

    #/dashboard/merchandise/add_product/
    url(r'^add_product/', views.ProductCreate.as_view(), name="product-add"),

    #/dashboard/merchandise/update_product/
    url(r'^update_product/(?P<pk>[0-9]+)/$', views.ProductUpdate.as_view(), name="product-update"),

    #/dashboard/merchandise/[id]/delete_product
    url(r'^(?P<pk>[0-9]+)/delete_product/$', views.ProductDelete.as_view(), name="product-delete"),

    #--------------Tag URLS :

    # /dashboard/merchandise/tag/
    url(r'^tag/', views.TagView.as_view(), name='tag'),

    #/dashboard/merchandise/add_tag/
    url(r'^add_tag/', views.TagCreate.as_view(), name="tag-add"),

    #/dashboard/merchandise/update_tag/
    url(r'^update_tag/(?P<pk>[0-9]+)/$', views.TagUpdate.as_view(), name="tag-update"),

    #/dashboard/merchandise/[id]/delete_tag
    url(r'^(?P<pk>[0-9]+)/delete_tag/$', views.TagDelete.as_view(), name="tag-delete"), 



]
