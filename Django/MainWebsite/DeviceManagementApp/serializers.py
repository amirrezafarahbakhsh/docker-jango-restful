from rest_framework import serializers
from .models import DeviceInstance


class DeviceInstanceSerialier(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    owner_id = serializers.ReadOnlyField(source='owner.id')
    DeviceID = serializers.ReadOnlyField()
    connectionStatus = serializers.ReadOnlyField()
    class Meta:
        model = DeviceInstance
        fields = [
            'name',
            'DeviceID',
            'deviceModel',
            'ip',
            'owner',
            'owner_id',
            'location',
            'accessedUsers',
            'connectionStatus'
        ]
