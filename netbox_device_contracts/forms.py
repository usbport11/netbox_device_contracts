from django import forms
from django.forms import ModelChoiceField
from netbox.forms import NetBoxModelForm, NetBoxModelFilterSetForm
from utilities.forms import DateTimePicker, DynamicModelChoiceField
from dcim.models import Device
from .models import DeviceContract, DeviceContractDevices, DeviceContractStatusTypeChoices

class DeviceContractForm(NetBoxModelForm):
    class Meta:
        model = DeviceContract
        fields = ('name', 'number', 'status', 'start', 'end', 'comments', 'tags')
        widgets = {
            'start': DateTimePicker(),
            'end': DateTimePicker()
        }

class DeviceContractDevicesForm(NetBoxModelForm):
    serial = forms.CharField(
        max_length = 30,
        required = False
    )
    device = DynamicModelChoiceField(
        queryset=Device.objects.all(),
        query_params = {
            'serial': '$serial',
        }
    )
    class Meta:
        model = DeviceContractDevices
        fields = ('device_contract', 'serial', 'device', 'tags')

class DeviceContractFilterForm(NetBoxModelFilterSetForm):
    model = DeviceContract

    name = forms.CharField(
        required=False
    )

    number = forms.CharField(
        required=False
    )

    status = forms.MultipleChoiceField(
        choices=DeviceContractStatusTypeChoices,
        required=False
    )

    start = forms.CharField(
        required=False
    )

    end = forms.CharField(
        required=False
    )

class DeviceContractDevicesFilterForm(NetBoxModelFilterSetForm):
    model = DeviceContractDevices

    device_contract = DynamicModelChoiceField(
        queryset=DeviceContract.objects.all(),
        required=False
    )

    device = DynamicModelChoiceField(
        queryset=Device.objects.all(),
        required=False
    )
