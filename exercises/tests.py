from django.utils import timezone
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Exercise, ExerciseLog


class ExerciseLogDetailTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client.login(username='testuser', password='12345')
        self.exercise = Exercise.objects.create(title='Test Exercise', description='Description')

    def test_exercise_log_detail(self):
        exercise_log = ExerciseLog.objects.create(
            user=self.user,
            exercise=self.exercise,
            date=timezone.now(),
        )

        url = reverse('exercise_log_detail', args=[exercise_log.id])
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
