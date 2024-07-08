from ..mixins import HospitalGenericViewSet
from rest_framework import mixins

from ..models import FinancialRecord
from ..serializers import FinanceRecordSerializer, FinanceRecordListSerializer


class FinanceView(
    HospitalGenericViewSet,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin
):
    lookup_field = 'id'

    def get_action_permission(self):
        if self.action in ('list', 'create'):
            self.action_permissions = []

    def get_serializer_class(self):
        if self.action == 'list':
            return FinanceRecordListSerializer
        if self.action == 'create':
            return FinanceRecordSerializer

    def get_queryset(self):
        return FinancialRecord.objects.all()