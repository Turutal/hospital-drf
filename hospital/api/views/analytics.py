from .. import models
from django.db.models import Avg, Sum, Count
from rest_framework import status
from rest_framework.response import Response
from ..mixins import HospitalGenericViewSet
from ..models import Patient, Doctor, Visit, Feedback, FinancialRecord


class AnalyticView(
    HospitalGenericViewSet
):

    def get_action_permission(self):
        if self.action == 'get_analytics':
            self.action_permissions = []

    def get_analytics(self, request):
        total_patients = Patient.objects.count()
        total_doctors = Doctor.objects.count()
        department_load = total_patients / total_doctors
        patient_satisfaction = Feedback.objects.aggregate(avg_rating=Avg('rating'))['avg_rating']
        total_revenue = FinancialRecord.objects.aggregate(avg_revenue=Avg('revenue'))['avg_revenue']
        total_expenses = FinancialRecord.objects.aggregate(avg_expenses=Avg('expenses'))['avg_expenses']
        total_profit = total_revenue - total_expenses

        data = {
            'total_patients': total_patients,
            'total_doctors': total_doctors,
            'department_load': department_load,
            'patient_satisfaction': patient_satisfaction,
            'total_revenue': total_revenue,
            'total_expenses': total_expenses,
            'total_profit': total_profit
        }

        return Response(status=status.HTTP_200_OK, data=data)
