from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import Department


@login_required
def departments_home(request):
    departments_list = Department.objects.all()
    return render(request, 'departments/departments.html', {'departments': departments_list})

