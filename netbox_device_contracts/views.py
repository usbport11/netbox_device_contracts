from netbox.views import generic
from django.db.models import Count
from . import filtersets, forms, models, tables

class DeviceContractView(generic.ObjectView):
    queryset = models.DeviceContract.objects.all()
    def get_extra_context(self, request, instance):
        table = tables.DeviceContractDevicesTable(instance.contract_devices.all())
        table.configure(request)
        return {
            'contract_devices_table': table,
        }

class DeviceContractListView(generic.ObjectListView):
    queryset = models.DeviceContract.objects.all()
    table = tables.DeviceContractTable
    filterset = filtersets.DeviceContractFilterSet
    filterset_form = forms.DeviceContractFilterForm

class DeviceContractEditView(generic.ObjectEditView):
    queryset = models.DeviceContract.objects.all()
    form = forms.DeviceContractForm

class DeviceContractDeleteView(generic.ObjectDeleteView):
    queryset = models.DeviceContract.objects.all()


class DeviceContractDevicesView(generic.ObjectView):
    queryset = models.DeviceContractDevices.objects.all()

class DeviceContractDevicesListView(generic.ObjectListView):
    queryset = models.DeviceContractDevices.objects.all()
    table = tables.DeviceContractDevicesTable
    filterset = filtersets.DeviceContractDevicesFilterSet
    filterset_form = forms.DeviceContractDevicesFilterForm

class DeviceContractDevicesEditView(generic.ObjectEditView):
    queryset = models.DeviceContractDevices.objects.all()
    form = forms.DeviceContractDevicesForm

class DeviceContractDevicesDeleteView(generic.ObjectDeleteView):
    queryset = models.DeviceContractDevices.objects.all()
