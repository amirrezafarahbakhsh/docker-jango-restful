from django.contrib import admin
from .models import DeviceInstance, DeviceModel, Location
# Register your models here.
admin.site.register(DeviceModel)
admin.site.register(DeviceInstance)
admin.site.register(Location)
