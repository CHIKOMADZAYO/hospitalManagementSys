from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def payments_home(request):
    invoices = [
        {'patient': 'Grace Moyo', 'amount': '$480.00', 'status': 'Paid', 'date': '2026-11-05'},
        {'patient': 'Ethan Smith', 'amount': '$1,260.00', 'status': 'Pending', 'date': '2026-11-08'},
        {'patient': 'Lily Adams', 'amount': '$310.00', 'status': 'Paid', 'date': '2026-11-06'},
        {'patient': 'Noah Patel', 'amount': '$890.00', 'status': 'Review', 'date': '2026-11-07'},
    ]
    return render(request, 'payments/payments.html', {'invoices': invoices})
