from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.


class DeviceModel(models.Model):
    name = models.TextField(max_length=50)

    def __str__(self) -> str:
        return f'Device : {self.name}'


class Location(models.Model):
    name = models.TextField(max_length=50)

    def __str__(self) -> str:
        return f'It\'s in the {self.name}'


class DeviceInstance(models.Model):
    name = models.CharField(max_length=50)
    DeviceID = models.UUIDField(primary_key=True, default=uuid.uuid4)
    deviceModel = models.ForeignKey('DeviceModel', on_delete=models.RESTRICT)
    ip = models.GenericIPAddressField(protocol='IPv4')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=False)
    location = models.ForeignKey(
        'Location', on_delete=models.SET_NULL, null=True)
    accessedUsers = models.ManyToManyField(User, related_name='accessedGroup')

    DEVICE_Connection_STATUS = (
        ('C', 'Connedcted'),
        ('D', 'Disconnected'),
        ('U', 'UnRegistered')
    )

    connectionStatus = models.CharField(
        max_length=1, choices=DEVICE_Connection_STATUS, blank=False, default='U')

    class Meta:
        ordering = ['name']

    def __str__(self) -> str:
        return f'The connection status of the {self.name} with ID {self.DeviceID} is: {self.connectionStatus}'
