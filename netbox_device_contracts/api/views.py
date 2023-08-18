from netbox.api.viewsets import NetBoxModelViewSet

from .. import models, filtersets
from .serializers import DeviceContractSerializer, DeviceContractDevicesSerializer

class DeviceContractViewSet(NetBoxModelViewSet):
    queryset = models.DeviceContract.objects.prefetch_related('tags')
    serializer_class = DeviceContractSerializer
    filterset_class = filtersets.DeviceContractFilterSet

class DeviceContractDevicesViewSet(NetBoxModelViewSet):
    queryset = models.DeviceContractDevices.objects.prefetch_related('tags')
    serializer_class = DeviceContractDevicesSerializer
    filterset_class = filtersets.DeviceContractDevicesFilterSet
