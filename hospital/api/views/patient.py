from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from ..mixins import HospitalGenericViewSet
from rest_framework import mixins

from ..models import Patient
from ..serializers import PatientListSerializer, PatientRetrieveSerializer, PatientCreateOrUpdateSerializer


class PatientView(
    HospitalGenericViewSet,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin
):
    lookup_field = 'id'

    filter_backends = [DjangoFilterBackend, filters.SearchFilter]

    filterset_fields = ['first_name', 'last_name']
    search_fields = ['first_name', 'last_name', 'gender']

    def get_action_permission(self):
        if self.action in ('list', 'retrieve'):
            self.action_permissions = ['view_patient']
        elif self.action == 'create':
            self.action_permissions = ['add_patient']
        elif self.action == 'update':
            self.action_permissions = ['change_patient']
        elif self.action == 'destroy':
            self.action_permissions = ['delete_patient']
        else:
            self.action_permissions = []

    def get_serializer_class(self):
        if self.action == 'list':
            return PatientListSerializer
        if self.action == 'retrieve':
            return PatientRetrieveSerializer
        if self.action == 'create':
            return PatientCreateOrUpdateSerializer
        if self.action == 'update':
            return PatientCreateOrUpdateSerializer

    def get_queryset(self):
        return Patient.objects.all()