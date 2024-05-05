from django.urls import path
from . import views


urlpatterns = [
    path('', views.subscriptions_view, name='subscriptions'),
    path('config/', views.stripe_config),
    path('create-checkout-session/', views.create_checkout_session),
    path('success/', views.success),  # new
    path('cancel/', views.cancel),  # new
]
