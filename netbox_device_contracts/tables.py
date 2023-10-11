import django_tables2 as tables
from netbox.tables import NetBoxTable, ChoiceFieldColumn
from .models import DeviceContract, DeviceContractDevices

class DeviceContractTable(NetBoxTable):
    name = tables.Column(
        linkify=True
    )
    status = ChoiceFieldColumn()

    class Meta(NetBoxTable.Meta):
        model = DeviceContract
        fields = ('pk', 'id', 'name', 'number', 'status', 'start', 'end', 'comments', 'actions')
        default_columns = ('name', 'number', 'status', 'start', 'end', 'comments', 'actions')

class DeviceContractDevicesTable(NetBoxTable):
    device_contract = tables.Column(
        linkify=True
    )
    device = tables.Column(
        linkify=True
    )

    class Meta(NetBoxTable.Meta):
        model = DeviceContractDevices
        fields = ('pk', 'id', 'device_contract', 'device', 'actions')
        default_columns = ('device', 'device_contract', 'actions')
