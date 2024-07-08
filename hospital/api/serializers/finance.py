from rest_framework import serializers
from ..models import FinancialRecord


class FinanceRecordListSerializer(serializers.Serializer):
    get_record = serializers.CharField()


class FinanceRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = FinancialRecord
        fields = '__all__'

