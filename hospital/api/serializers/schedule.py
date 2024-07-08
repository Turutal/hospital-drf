from rest_framework import serializers
from ..models import DoctorSchedule


class DoctorScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorSchedule
        fields = '__all__'


class DoctorScheduleUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorSchedule
        fields = ['day_of_week', 'start_time', 'end_time']

