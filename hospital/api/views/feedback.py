from ..mixins import HospitalGenericViewSet
from rest_framework import mixins

from ..models import Feedback
from ..serializers import FeedbackSerializer


class FeedbackView(
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
            return FeedbackSerializer
        if self.action == 'create':
            return FeedbackSerializer

    def get_queryset(self):
        return Feedback.objects.all()