from django.test import TestCase
from django.urls import reverse
from .models import Product


class ProductsPageTest(TestCase):
    def setUp(self):
        # Create some sample products for testing
        self.product1 = Product.objects.create(
            name='Test Product 1',
            price=10.00,
        )
        self.product2 = Product.objects.create(
            name='Test Product 2',
            price=20.00,
        )

    def test_products_page_rendering(self):
        response = self.client.get(reverse('products'))
        self.assertEqual(response.status_code, 200)

        # Check if the products are rendered on the page
        self.assertContains(response, self.product1.name)
        self.assertContains(response, self.product2.name)
