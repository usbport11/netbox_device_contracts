# Generated by Django 4.1.5 on 2023-10-10 08:21

from django.db import migrations, models
import django.db.models.deletion
import taggit.managers
import utilities.json


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('dcim', '0167_module_status'),
        ('extras', '0084_staging'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeviceContract',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('custom_field_data', models.JSONField(blank=True, default=dict, encoder=utilities.json.CustomFieldJSONEncoder)),
                ('name', models.CharField(max_length=100)),
                ('number', models.CharField(max_length=200)),
                ('status', models.CharField(max_length=30)),
                ('start', models.DateTimeField(max_length=100)),
                ('end', models.DateTimeField(blank=True, max_length=100, null=True)),
                ('comments', models.TextField(blank=True)),
                ('tags', taggit.managers.TaggableManager(through='extras.TaggedItem', to='extras.Tag')),
            ],
            options={
                'ordering': ('name', 'number', 'status'),
            },
        ),
        migrations.CreateModel(
            name='DeviceContractDevices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('custom_field_data', models.JSONField(blank=True, default=dict, encoder=utilities.json.CustomFieldJSONEncoder)),
                ('device', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='dcim.device')),
                ('device_contract', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contract_devices', to='netbox_device_contracts.devicecontract')),
                ('tags', taggit.managers.TaggableManager(through='extras.TaggedItem', to='extras.Tag')),
            ],
            options={
                'ordering': ('device',),
            },
        ),
    ]