from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from doctors.models import Doctor
from patients.models import Patients
from .models import UserProfile


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    role = forms.ChoiceField(choices=UserProfile.ROLE_CHOICES, required=True)
    phone = forms.CharField(max_length=20, required=False)
    doctor = forms.ModelChoiceField(queryset=Doctor.objects.none(), required=False)
    patient = forms.ModelChoiceField(queryset=Patients.objects.none(), required=False)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'role', 'phone', 'doctor', 'patient')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['doctor'].queryset = Doctor.objects.all()
        self.fields['patient'].queryset = Patients.objects.all()

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
            profile = UserProfile.objects.create(
                user=user,
                role=self.cleaned_data['role'],
                phone=self.cleaned_data.get('phone'),
                doctor=self.cleaned_data.get('doctor'),
                patient=self.cleaned_data.get('patient'),
            )
            profile.save()
        return user
