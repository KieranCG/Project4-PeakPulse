from django.conf import settings
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib import messages
from subscriptions.models import StripeCustomer
import stripe


def subscription_required(view_func):
    def _wrapped_view(request, *args, **kwargs):
        # Get the current user
        user = request.user

        # Check if the user is authenticated
        if not user.is_authenticated:
            messages.error(request, 'You need to be logged in to access this page.')
            return redirect(reverse('account_login'))  # Redirect to login page if user is not logged in

        # Check if the user has a StripeCustomer profile
        try:
            stripe_customer = StripeCustomer.objects.get(user=user)
        except StripeCustomer.DoesNotExist:
            messages.error(request, 'You need to have a subscription to access this page.')
            return redirect(reverse('subscriptions_signup'))  # Redirect to subscription signup page if user does not have a profile

        # Check the subscription status using Stripe API
        stripe.api_key = settings.STRIPE_SECRET_KEY
        try:
            subscription = stripe.Subscription.retrieve(stripe_customer.stripeSubscriptionId)
        except stripe.error.StripeError as e:
            messages.error(request, 'Error retrieving subscription information.')
            # Log the error for debugging purposes
            print(f"Stripe API Error: {e}")
            return redirect(reverse('home'))  # Redirect to home page or an appropriate error page

        # Check if the subscription status is active
        if subscription.status != 'active':
            messages.error(request, 'Your subscription is inactive. Please renew your subscription to access this page.')
            return redirect(reverse('subscription_inactive'))  # Redirect to inactive subscription page if subscription is not active

        # If subscription status is active, allow access to the view
        return view_func(request, *args, **kwargs)

    return _wrapped_view
