from rest_framework import serializers

from ..models import Patient


class PatientListSerializer(serializers.Serializer):
    full_name = serializers.CharField()
    contact_info = serializers.CharField()


class PatientRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'


class PatientCreateOrUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'

