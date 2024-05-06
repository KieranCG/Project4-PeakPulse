from django.test import TestCase
from django.urls import reverse


class SuccessTemplateTestCase(TestCase):
    def test_success_template_content(self):
        url = 'success/'  # Use the actual URL path for the 'success' view
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'subscriptions/success.html')  # Make sure the correct template is used

        # Check for expected content in the response HTML
        self.assertContains(response, '<h2 class="logo-font">Congratulations!</h2>')
        self.assertContains(response, '<p class="success-message">You\'ve successfully subscribed to our premium service! 🎉</p>')
        self.assertContains(response, '<a href="{% url \'home\' %}" class="btn btn-primary btn-lg">Return to the dashboard</a>')
