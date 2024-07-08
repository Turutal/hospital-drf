from django.contrib import admin

from .models import Specialization, Service, Visit, Patient, DoctorSchedule

# Register your models here.

admin.site.register(Specialization)
admin.site.register(Service)
admin.site.register(Visit)
admin.site.register(Patient)
admin.site.register(DoctorSchedule)