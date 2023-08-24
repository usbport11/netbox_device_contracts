from netbox.filtersets import NetBoxModelFilterSet
from .models import DeviceContract, DeviceContractDevices


class DeviceContractFilterSet(NetBoxModelFilterSet):
    class Meta:
        model = DeviceContract
        fields = ('id', 'name', 'number', 'status', 'start', 'end', 'comments')

    def search(self, queryset, name, value):
        return queryset.filter(name__icontains=value)

class DeviceContractDevicesFilterSet(NetBoxModelFilterSet):
    class Meta:
        model = DeviceContractDevices
        fields = ('id', 'device_contract', 'device')

    def search(self, queryset, name, value):
        return queryset.filter(device__name__icontains=value)
