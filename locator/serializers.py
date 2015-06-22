from locator.models import Location
from rest_framework import serializers as ser


class LocationSerializer(ser.HyperlinkedModelSerializer):
    class Meta:
        model = Location
        fields = ['name', 'longitude', 'latitude', 'last_sought']