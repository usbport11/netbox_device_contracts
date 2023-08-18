from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.urls import reverse

from netbox.models import NetBoxModel
from utilities.choices import ChoiceSet

class DeviceContractStatusTypeChoices(ChoiceSet):
    key = 'DeviceContract.status'

    CHOICES = [
        ('open', 'Open', 'green'),
        ('hold', 'Hold', 'orange'),
        ('closed', 'Closed', 'indigo'),
        ('reject', 'Reject', 'red'),
    ]

class DeviceContract(NetBoxModel):
    name = models.CharField(
        max_length=100,
        verbose_name="Contract Name",
    )
    number = models.CharField(
        max_length=200,
        verbose_name="Contract Number",
    )
    status = models.CharField(
        max_length=30,
        choices=DeviceContractStatusTypeChoices,
    )
    start = models.DateTimeField(
        max_length=100,
    )
    end = models.DateTimeField(
        max_length=100,
        null=True,
        blank=True,
    )
    comments = models.TextField(
        blank=True
    )

    class Meta:
        ordering = ('name', 'number', 'status')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('plugins:netbox_device_contracts:devicecontract', args=[self.pk])

    def get_status_color(self):
        return DeviceContractStatusTypeChoices.colors.get(self.status)

class DeviceContractDevices(NetBoxModel):
    device_contract = models.ForeignKey(
        to=DeviceContract,
        on_delete=models.CASCADE,
        related_name='contract_devices'
    )
    device = models.ForeignKey(
        to='dcim.Device',
        on_delete=models.CASCADE,
        related_name='+',
        default=None
    )

    class Meta:
        ordering = ('device',)
        unique_together = ('device',)

    def __str__(self):
        return self.device_contract.name

    def get_absolute_url(self):
        return reverse('plugins:netbox_device_contracts:devicecontractdevices', args=[self.pk])

    def get_default_action_color(self):
        return ActionChoices.colors.get(self.default_action)
