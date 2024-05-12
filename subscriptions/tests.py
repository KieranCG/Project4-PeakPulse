from django.test import TestCase
from django.urls import reverse


class HomePageViewTestCase(TestCase):
    def test_home_page_view(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

        # Check for the actual templates used
        actual_templates = [template.name for template in response.templates]

        # Check if any of the expected templates are used in the response
        expected_templates = ['home/index.html', 'base.html', 'includes/mobile-top-header.html', 'includes/main-nav.html']
        for template in expected_templates:
            self.assertIn(template, actual_templates, f"Expected template '{template}' was not used to render the response.")


class SimpleTestCase(TestCase):
    def test_testing_setup(self):
        # Checking testing environment
        self.assertTrue(True)
