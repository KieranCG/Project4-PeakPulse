from django.test import TestCase
from django.urls import reverse


class ShoppingBagPageTest(TestCase):
    def test_shopping_bag_page_rendering(self):
        response = self.client.get(reverse('view_bag'))
        self.assertEqual(response.status_code, 200)
