from rest_framework import serializers

from dcim.api.nested_serializers import NestedDeviceSerializer
from netbox.api.serializers import NetBoxModelSerializer, WritableNestedSerializer
from ..models import DeviceContract, DeviceContractDevices

#
# Nested serializers
#

class NestedDeviceContractSerializer(WritableNestedSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_device_contracts-api:devicecontract-detail'
    )

    class Meta:
        model = DeviceContract
        fields = ('id', 'url', 'display', 'name')

class NestedDeviceContractDevicesSerializer(WritableNestedSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_device_contracts-api:devicecontractdevices-detail'
    )

    class Meta:
        model = DeviceContractDevices
        fields = ('id', 'url', 'display')

#
# Regular serializers
#

class DeviceContractSerializer(NetBoxModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_device_contracts-api:devicecontract-detail'
    )

    class Meta:
        model = DeviceContract
        fields = (
            'id', 'url', 'display', 'name', 'number', 'status', 'start', 'end', 'comments', 'tags', 'custom_fields', 
            'created', 'last_updated',
        )

class DeviceContractDevicesSerializer(NetBoxModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_device_contracts-api:devicecontractdevices-detail'
    )

    device = NestedDeviceSerializer()

    class Meta:
        model = DeviceContractDevices
        fields = (
            'id', 'url', 'display', 'device_contract', 'device', 'tags', 'custom_fields', 
            'created', 'last_updated',
        )
