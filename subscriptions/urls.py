from django.urls import path
from . import views

app_name = 'subscriptions'


urlpatterns = [
    path('', views.subscriptions_view, name='subscriptions'),
    path('checkout/', views.subscription_checkout, name='subscription_checkout'),
]
