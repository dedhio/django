from django.conf.urls import url


from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^custom/', views.custom, name='custom'),
    url(r'^vehicle/add/$', views.VehicleCreate.as_view(), name='vehicle_add'),
    url(r'^vehicle/(?P<pk>\d+)/edit/$', views.VehicleUpdate.as_view(), name='vehicle_update'),
    url(r'^vehicle/(?P<pk>\d+)/delete/$', views.VehicleDelete.as_view(), name='vehicle_delete'),
    url(r'^vehicle/$', views.VehicleListView.as_view(), name='vehicle_list'),
    url(r'^vehicle/(?P<pk>\d+)/$', views.VehicleDetailView.as_view(), name='vehicle_detail'),
    url(r'^vehicle_validate/(?P<pk>\d+)/$', views.VehicleRedirectView.as_view(), name='vehicle_redirect'),
    url(r'^usecontrol/list/', views.UseControlList.as_view(), name='use_control_list'),
    #url(r'^usecontrol/add/', views.use_control_add, name='use_control_add'),
    #url(r'^usecontrol/list/', views.use_control_list, name='use_control_list'),
]