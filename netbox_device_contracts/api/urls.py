from netbox.api.routers import NetBoxRouter
from . import views

app_name = 'netbox_device_contracts'

router = NetBoxRouter()
router.register('device-contracts', views.DeviceContractViewSet)
router.register('device-contracts-devices', views.DeviceContractDevicesViewSet)

urlpatterns = router.urls
