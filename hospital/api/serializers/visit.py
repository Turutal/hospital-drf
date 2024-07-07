from rest_framework import serializers
from ..models import Visit


class VisitListSerializer(serializers.Serializer):
    get_info = serializers.CharField()
    service = serializers.CharField()


class VisitRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visit
        fields = '__all__'


class VisitCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visit
        fields = '__all__'


class VisitUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visit
        fields = ['visit_date_time']
