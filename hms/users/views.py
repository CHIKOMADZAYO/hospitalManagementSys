from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect, render

from .forms import CustomUserCreationForm
from .models import UserProfile


class CustomLoginView(LoginView):
    template_name = 'users/login.html'
    authentication_form = AuthenticationForm

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, f'Welcome back, {self.request.user.username}!')
        return response


class CustomLogoutView(LogoutView):
    next_page = 'dashboard_home'


def users_home(request):
    return render(request, 'users/home.html')


def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Your account has been created successfully.')
            return redirect('profile')
    else:
        form = CustomUserCreationForm()

    return render(request, 'users/register.html', {'form': form})


@login_required
def profile_view(request):
    profile, _ = UserProfile.objects.get_or_create(user=request.user)

    from doctors.models import Doctor
    from patients.models import Patients

    doctors = Doctor.objects.all()
    patients = Patients.objects.all()

    if request.method == 'POST':
        role = request.POST.get('role')
        phone = request.POST.get('phone')
        doctor = request.POST.get('doctor')
        patient = request.POST.get('patient')

        if role:
            profile.role = role
        if phone is not None:
            profile.phone = phone
        profile.doctor_id = doctor or None
        profile.patient_id = patient or None

        profile.save()
        messages.success(request, 'Your profile was updated successfully.')
        return redirect('profile')

    return render(request, 'users/profile.html', {'profile': profile, 'doctors': doctors, 'patients': patients})
