from django.urls import path

from .views import appointments_home, create_appointment, delete_appointment, edit_appointment


urlpatterns = [
    path('', appointments_home, name='appointments_home'),
    path('create/', create_appointment, name='create_appointment'),
    path('edit/<int:pk>/', edit_appointment, name='edit_appointment'),
    path('delete/<int:pk>/', delete_appointment, name='delete_appointment'),
]