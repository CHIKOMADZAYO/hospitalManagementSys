from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from appointments.models import Appointment
from doctors.models import Doctor
from patients.models import Patients
from users.models import UserProfile


@login_required
def dashboard_home(request):
    profile, _ = UserProfile.objects.get_or_create(user=request.user)
    role = profile.role

    doctor_count = Doctor.objects.count()
    patient_count = Patients.objects.count()
    appointment_count = Appointment.objects.count()
    scheduled_count = Appointment.objects.filter(status='scheduled').count()
    completed_count = Appointment.objects.filter(status='completed').count()
    recent_appointments = Appointment.objects.select_related('patient', 'doctor').order_by('-appointment_date')[:5]

    dashboard_context = {
        'profile': profile,
        'doctor_count': doctor_count,
        'patient_count': patient_count,
        'appointment_count': appointment_count,
        'scheduled_count': scheduled_count,
        'completed_count': completed_count,
        'recent_appointments': recent_appointments,
    }

    if role == 'doctor':
        return render(request, 'dashboard/doctor_dashboard.html', dashboard_context)
    if role == 'patient':
        return render(request, 'dashboard/patient_dashboard.html', dashboard_context)

    return render(request, 'dashboard/admin_dashboard.html', dashboard_context)
