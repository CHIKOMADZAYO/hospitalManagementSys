from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .models import Doctor


@login_required
def doctor_home(request):
    doctors = Doctor.objects.order_by('name')
    return render(request, 'doctors/doctors.html', {'doctors': doctors})


@login_required
def create_doctor(request):
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        specialization = request.POST.get('specialization', '').strip()
        email = request.POST.get('email', '').strip()
        phone_number = request.POST.get('phone_number', '').strip()

        if name and specialization and email and phone_number:
            Doctor.objects.create(
                name=name,
                specialization=specialization,
                email=email,
                phone_number=phone_number,
            )
            messages.success(request, 'Doctor added successfully.')
            return redirect('doctor_home')

        messages.error(request, 'Please fill in all required fields.')

    return render(request, 'doctors/create_doctor.html')


@login_required
def edit_doctor(request, pk):
    doctor = get_object_or_404(Doctor, pk=pk)

    if request.method == 'POST':
        doctor.name = request.POST.get('name', doctor.name).strip()
        doctor.specialization = request.POST.get('specialization', doctor.specialization).strip()
        doctor.email = request.POST.get('email', doctor.email).strip()
        doctor.phone_number = request.POST.get('phone_number', doctor.phone_number).strip()

        if doctor.name and doctor.specialization and doctor.email and doctor.phone_number:
            doctor.save()
            messages.success(request, 'Doctor updated successfully.')
            return redirect('doctor_home')

        messages.error(request, 'Please fill in all required fields.')

    return render(request, 'doctors/create_doctor.html', {'doctor': doctor, 'is_edit': True})


@login_required
def delete_doctor(request, pk):
    doctor = get_object_or_404(Doctor, pk=pk)
    if request.method == 'POST':
        doctor.delete()
        messages.success(request, f'{doctor.name} was removed from the medical staff.')
    return redirect('doctor_home')
