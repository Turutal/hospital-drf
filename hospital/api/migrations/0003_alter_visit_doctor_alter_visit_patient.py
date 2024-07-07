# Generated by Django 5.0.6 on 2024-07-05 09:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0002_doctor_patient_service_specialization_visit_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="visit",
            name="doctor",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="visits",
                to="api.doctor",
            ),
        ),
        migrations.AlterField(
            model_name="visit",
            name="patient",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="visits",
                to="api.patient",
            ),
        ),
    ]