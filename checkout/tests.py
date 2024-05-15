from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from .models import Order


class CheckoutSuccessPageTest(TestCase):
    def setUp(self):
        # Create a sample order to use in the test
        self.order = Order.objects.create(
            order_number='123456',
            date=timezone.now(),
        )

    def test_checkout_success_page_rendering(self):
        response = self.client.get(reverse('checkout_success', args=[self.order.order_number]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'checkout/checkout_success.html')
