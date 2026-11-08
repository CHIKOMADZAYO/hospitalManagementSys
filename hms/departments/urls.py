from django.urls import path

from .views import departments_home


urlpatterns = [
    path('', departments_home, name='departments_home'),
]