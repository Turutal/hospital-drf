from ..mixins import HospitalGenericViewSet
from rest_framework import mixins

from ..models import DoctorSchedule
from ..serializers import DoctorScheduleSerializer, DoctorScheduleUpdateSerializer


class ScheduleView(
    HospitalGenericViewSet,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin
):
    lookup_field = 'id'

    def get_action_permission(self):
        if self.action in ('list', 'retrieve'):
            self.action_permissions = ['view_doctorschedule']
        elif self.action == 'create':
            self.action_permissions = ['add_doctorschedule']
        elif self.action == 'update':
            self.action_permissions = ['change_doctorschedule']
        elif self.action == 'destroy':
            self.action_permissions = ['delete_doctorschedule']
        else:
            self.action_permissions = []

    def get_serializer_class(self):
        if self.action == 'list':
            return DoctorScheduleSerializer
        if self.action == 'retrieve':
            return DoctorScheduleSerializer
        if self.action == 'create':
            return DoctorScheduleSerializer
        if self.action == 'update':
            return DoctorScheduleUpdateSerializer
        if self.action == 'delete':
            return DoctorScheduleSerializer

    def get_queryset(self):
        return DoctorSchedule.objects.all()