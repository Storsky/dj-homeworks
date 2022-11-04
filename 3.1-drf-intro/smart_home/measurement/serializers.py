from rest_framework import serializers
from .models import Measurement, Sensor

class MeasurmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ['sensor_id', 'measure', 'stamp']

class SensorMeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ['measure', 'stamp']


class SensorSerializer(serializers.ModelSerializer):
    measurements = SensorMeasurementSerializer(many = True)
    class Meta:
        model = Sensor
        fields = ['name', 'description', 'measurements']

