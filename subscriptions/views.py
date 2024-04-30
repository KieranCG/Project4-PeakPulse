from django.shortcuts import render


def subscriptions_view(request):
    """ View function to render subscriptions.html template """
    return render(request, 'subscriptions/subscriptions.html')
