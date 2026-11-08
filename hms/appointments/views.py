from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from doctors.models import Doctor
from patients.models import Patients
from .models import Appointment


@login_required
def appointments_home(request):
    appointments = Appointment.objects.select_related('patient', 'doctor').order_by('-appointment_date')
    return render(request, 'appointments/appointments.html', {'appointments': appointments})


@login_required
def create_appointment(request):
    doctors = Doctor.objects.all()
    patients = Patients.objects.all()

    if request.method == 'POST':
        patient_id = request.POST.get('patient')
        doctor_id = request.POST.get('doctor')
        appointment_date = request.POST.get('appointment_date')
        status = request.POST.get('status', 'scheduled')
        notes = request.POST.get('notes', '')

        if patient_id and doctor_id and appointment_date:
            patient = Patients.objects.get(id=patient_id)
            doctor = Doctor.objects.get(id=doctor_id)

            Appointment.objects.create(
                patient=patient,
                doctor=doctor,
                appointment_date=appointment_date,
                status=status,
                notes=notes,
            )
            messages.success(request, 'Appointment created successfully.')
            return redirect('appointments_home')

        messages.error(request, 'Please fill in all required fields.')

    return render(request, 'appointments/create_appointment.html', {
        'doctors': doctors,
        'patients': patients,
        'is_edit': False,
    })


@login_required
def edit_appointment(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk)
    doctors = Doctor.objects.all()
    patients = Patients.objects.all()

    if request.method == 'POST':
        patient_id = request.POST.get('patient')
        doctor_id = request.POST.get('doctor')
        appointment_date = request.POST.get('appointment_date')
        status = request.POST.get('status', 'scheduled')
        notes = request.POST.get('notes', '')

        if patient_id and doctor_id and appointment_date:
            appointment.patient_id = patient_id
            appointment.doctor_id = doctor_id
            appointment.appointment_date = appointment_date
            appointment.status = status
            appointment.notes = notes
            appointment.save()
            messages.success(request, 'Appointment updated successfully.')
            return redirect('appointments_home')

        messages.error(request, 'Please fill in all required fields.')

    return render(request, 'appointments/create_appointment.html', {
        'appointment': appointment,
        'doctors': doctors,
        'patients': patients,
        'is_edit': True,
    })


@login_required
def delete_appointment(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk)
    if request.method == 'POST':
        label = f'{appointment.patient} with {appointment.doctor}'
        appointment.delete()
        messages.success(request, f'Appointment for {label} was removed.')
    return redirect('appointments_home')
