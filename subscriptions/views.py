from django.shortcuts import render


def subscriptions_view(request):
    """ View function to render subscriptions.html template """
    return render(request, 'subscriptions/subscriptions.html')


def subscription_checkout(request):
    """ View logic for the subscription checkout page """
    return render(request, 'subscriptions/subscriptions_checkout.html')
