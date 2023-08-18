from extras.plugins import PluginMenuButton, PluginMenuItem
from utilities.choices import ButtonColorChoices


devicecontract_buttons = [
    PluginMenuButton(
        link='plugins:netbox_device_contracts:devicecontract_add',
        title='Add',
        icon_class='mdi mdi-plus-thick',
        color=ButtonColorChoices.GREEN
    )
]

devicecontractdevices_buttons = [
    PluginMenuButton(
        link='plugins:netbox_device_contracts:devicecontractdevices_add',
        title='Add',
        icon_class='mdi mdi-plus-thick',
        color=ButtonColorChoices.GREEN
    )
]

menu_items = (
    PluginMenuItem(
        link='plugins:netbox_device_contracts:devicecontract_list',
        link_text='Device Contracts',
        buttons=devicecontract_buttons
    ),
    PluginMenuItem(
        link='plugins:netbox_device_contracts:devicecontractdevices_list',
        link_text='Device Contracts Devices',
        buttons=devicecontractdevices_buttons
    ),
)
