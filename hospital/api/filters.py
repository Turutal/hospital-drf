import django_filters as filters

from .models import Doctor


class DoctorFilterSet(filters.FilterSet):
    last_name = filters.CharFilter()

    class Meta:
        model = Doctor
        fields = {
            'last_name': ['exact', 'contains'],
            'first_name': ['contains'],
            'specialization': ['exact']
        }