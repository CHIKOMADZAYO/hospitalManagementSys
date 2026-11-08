from django.urls import path

from .views import PatientsView, delete_patient, edit_patient


urlpatterns = [
    path('', PatientsView.as_view(), name='patients'),
    path('edit/<int:pk>/', edit_patient, name='edit_patient'),
    path('delete/<int:pk>/', delete_patient, name='delete_patient'),
]

