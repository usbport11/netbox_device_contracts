from extras.plugins import PluginConfig

class NetBoxDeviceContractsConfig(PluginConfig):
    name = 'netbox_device_contracts'
    verbose_name = ' NetBox Device Contracts'
    description = 'Manage device contracts'
    version = '0.1'
    base_url = 'device-contracts'
    min_version = '3.3.0'

config = NetBoxDeviceContractsConfig
