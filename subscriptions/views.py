from django.shortcuts import render
from .models import FitnessPlan, Customer


def join(request):
    # Retrieve FitnessPlan objects
    plans = FitnessPlan.objects.all()
    
    # Pass plans to the template context
    return render(request, 'join.html', {'plans': plans})
