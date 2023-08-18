from django.urls import path
from netbox.views.generic import ObjectChangeLogView
from . import models, views

urlpatterns = (
    path('device-contracts/', views.DeviceContractListView.as_view(), name='devicecontract_list'),
    path('device-contracts/add/', views.DeviceContractEditView.as_view(), name='devicecontract_add'),
    path('device-contracts/<int:pk>/', views.DeviceContractView.as_view(), name='devicecontract'),
    path('device-contracts/<int:pk>/edit/', views.DeviceContractEditView.as_view(), name='devicecontract_edit'),
    path('device-contracts/<int:pk>/delete/', views.DeviceContractDeleteView.as_view(), name='devicecontract_delete'),
    path('device-contracts/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='devicecontract_changelog', kwargs={
        'model': models.DeviceContract
    }),
    
    path('device-contracts-devices/', views.DeviceContractDevicesListView.as_view(), name='devicecontractdevices_list'),
    path('device-contracts-devices/add/', views.DeviceContractDevicesEditView.as_view(), name='devicecontractdevices_add'),
    path('device-contracts-devices/<int:pk>/', views.DeviceContractDevicesView.as_view(), name='devicecontractdevices'),
    path('device-contracts-devices/<int:pk>/edit/', views.DeviceContractDevicesEditView.as_view(), name='devicecontractdevices_edit'),
    path('device-contracts-devices/<int:pk>/delete/', views.DeviceContractDevicesDeleteView.as_view(), name='devicecontractdevices_delete'),
    path('device-contracts-devices/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='devicecontractdevices_changelog', kwargs={
        'model': models.DeviceContractDevices
    }),
)
