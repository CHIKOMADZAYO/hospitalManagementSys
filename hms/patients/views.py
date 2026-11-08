from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.utils.decorators import method_decorator
from django.views import View

from .models import Patients


@method_decorator(login_required, name='dispatch')
class PatientsView(View):
    template_name = 'patients/patients.html'

    def get(self, request):
        patients = Patients.objects.order_by('last_name', 'first_name')
        return render(request, self.template_name, {'patients': patients})

    def post(self, request):
        first_name = request.POST.get('first_name', '').strip()
        last_name = request.POST.get('last_name', '').strip()
        email = request.POST.get('email', '').strip()
        phone = request.POST.get('phone', '').strip()
        date_of_birth = request.POST.get('date_of_birth', '').strip()
        gender = request.POST.get('gender', '').strip()
        address = request.POST.get('address', '').strip()

        if first_name and last_name:
            Patients.objects.create(
                first_name=first_name,
                last_name=last_name,
                email=email or None,
                phone=phone or None,
                date_of_birth=date_of_birth or None,
                gender=gender or None,
                address=address or None,
            )
            messages.success(request, 'Patient added successfully.')
        else:
            messages.error(request, 'First name and last name are required.')

        patients = Patients.objects.order_by('last_name', 'first_name')
        return render(request, self.template_name, {'patients': patients})


@login_required
def edit_patient(request, pk):
    patient = get_object_or_404(Patients, pk=pk)

    if request.method == 'POST':
        patient.first_name = request.POST.get('first_name', patient.first_name).strip()
        patient.last_name = request.POST.get('last_name', patient.last_name).strip()
        patient.email = request.POST.get('email', patient.email).strip() or None
        patient.phone = request.POST.get('phone', patient.phone).strip() or None
        patient.date_of_birth = request.POST.get('date_of_birth') or patient.date_of_birth
        patient.gender = request.POST.get('gender') or patient.gender
        patient.address = request.POST.get('address', patient.address).strip() or None

        if patient.first_name and patient.last_name:
            patient.save()
            messages.success(request, 'Patient updated successfully.')
            return redirect('patients')

        messages.error(request, 'First name and last name are required.')

    return render(request, 'patients/patient_form.html', {'patient': patient, 'is_edit': True})


@login_required
def delete_patient(request, pk):
    patient = get_object_or_404(Patients, pk=pk)
    if request.method == 'POST':
        name = f'{patient.first_name} {patient.last_name}'
        patient.delete()
        messages.success(request, f'{name} was removed from the patient list.')
    return redirect('patients')