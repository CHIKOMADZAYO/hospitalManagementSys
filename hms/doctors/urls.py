from django.urls import path

from .views import create_doctor, delete_doctor, doctor_home, edit_doctor


urlpatterns = [
    path('', doctor_home, name='doctor_home'),
    path('create/', create_doctor, name='create_doctor'),
    path('edit/<int:pk>/', edit_doctor, name='edit_doctor'),
    path('delete/<int:pk>/', delete_doctor, name='delete_doctor'),
]
