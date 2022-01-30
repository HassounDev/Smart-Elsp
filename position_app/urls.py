from django.conf.urls import  url
from . import views
from django.template import loader

app_name = 'position_app'
urlpatterns = [
#welcome

    url(r'^$',views.IndexView.as_view(), name='index'),
    url(r'member/$', views.MemberView.as_view(), name='member'),
    url(r'service/$', views.ServiceView.as_view(), name='service'),
    url(r'link/$', views.LinkView.as_view(), name='link'),
    url(r'point/$', views.PointView.as_view(), name='point'),
    url(r'coordonne/$', views.CoordView.as_view(), name='coordonne'),
    url(r'coordonne_cach/$',views.coordonnes_view, name='coordonne_cach'),
    url(r'show/$',views.Showv.as_view(), name='position_show'),
    url(r'position_cach/$',views.positions_view, name='position_cach'),
    url(r'coordonne/detail/(?P<pk>[0-9]+)/$',views.DetailCord.as_view(), name ='detail-cord'),



    url(r'position/add/$', views.PositionCreate.as_view(), name='position-add'),
    url(r'member/addmember/add/$', views.MemberCreate.as_view(), name='member-add'),
    url(r'service/addservice/add/$', views.ServiceCreate.as_view(), name='service-add'),
    url(r'link/addlink/add/$', views.LinkCreate.as_view(), name='link-add'),
    url(r'coordonne/add/$', views.CoordCreate.as_view(), name='coord-add'),
    url(r'digitalcord/add/$',views.CoordNumCreate.as_view(), name ='digcord-add'),
    url(r'personcontact/add/$',views.PerContactCreate.as_view(), name ='percontact-add'),
    #url(r'personcontact/add/$',views.PerContactCreate.as_view(), name ='PerContactUpdate-add'),

    url(r'member/(?P<pk>[0-9]+)/delete/$', views.MemberDelete.as_view(), name='member-delete'),
    url( r'^(?P<pk>[0-9]+)/delete/$', views.PositionDelete.as_view(), name='position-delete'),
    url(r'service/(?P<pk>[0-9]+)/delete/$', views.ServiceDelete.as_view(), name='service-delete'),
    url(r'link/(?P<pk>[0-9]+)/delete/$', views.LinkDelete.as_view(), name='link-delete'),
    url(r'coordonne/(?P<pk>[0-9]+)/delete/$', views.CoordDelete.as_view(), name='cord-delete'),
    url(r'digitalcord/(?P<pk>[0-9]+)/delete/$',views.CoordNumDelete.as_view(), name ='digcord-delete'),
    url(r'personcontact/(?P<pk>[0-9]+)/delete/$',views.PerContactDelete.as_view(), name ='percontact-delete'),

    url(r'^position/(?P<pk>[0-9]+)/$',views.PositionUpdate.as_view(),name='position-update'),
    url(r'member/addmember/(?P<pk>[0-9]+)/$',views.MemberUpdate.as_view(),name='member-update'),
    url(r'service/addservice/(?P<pk>[0-9]+)/$',views.ServiceUpdate.as_view(),name='service-update'),
    url(r'link/addlink/(?P<pk>[0-9]+)/$',views.LinkUpdate.as_view(),name='link-update'),
    url(r'coordonne/(?P<pk>[0-9]+)/$',views.CoordUpdate.as_view(),name='cord-update'),
    url(r'digitalcord/(?P<pk>[0-9]+)/$',views.CoordNumUpdate.as_view(), name ='digcord-update'),
    url(r'personcontact/(?P<pk>[0-9]+)/$',views.PerContactUpdate.as_view(), name ='percontact-update'),

]
