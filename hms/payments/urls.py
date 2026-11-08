from django.urls import path

from .views import payments_home


urlpatterns = [
    path('', payments_home, name='payments_home'),
]