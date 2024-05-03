from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Customer
from django.conf import settings
from django.http.response import JsonResponse # new
from django.views.decorators.csrf import csrf_exempt # new
import stripe


@login_required
def subscriptions_view(request):
    """ View function to render subscriptions.html template """
    return render(request, 'subscriptions/subscriptions.html')


@login_required
def subscription_checkout(request):
    """ View logic for the subscription checkout page """
    return render(request, 'subscriptions/subscriptions_checkout.html')
