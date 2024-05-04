from django.urls import path
from . import views


urlpatterns = [
    path('', views.subscriptions_view, name='subscriptions'),
    path('config/', views.stripe_config),  # new
    path('create-checkout-session/', views.create_checkout_session),  # new
]
