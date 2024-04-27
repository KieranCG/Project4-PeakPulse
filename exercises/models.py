from django.db import models
from django.contrib.auth.models import User


class ExerciseCategory(models.Model):

    class Meta:
        verbose_name_plural = 'Exercise Categories'

    name = models.CharField(max_length=100)
    friendly_name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Exercise(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)  # ForeignKey to link each exercise with a user
    title = models.CharField(max_length=200)
    description = models.TextField()
    bodypart = models.CharField(max_length=100)
    equipment = models.CharField(max_length=100)
    level = models.CharField(max_length=100)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    ratingdesc = models.CharField(max_length=200)
    category = models.ForeignKey(ExerciseCategory, null=True, blank=True, on_delete=models.SET_NULL)

    # Additional Fields
    sets = models.PositiveIntegerField(default=1)
    repetitions = models.PositiveIntegerField(default=1)
    duration = models.DurationField(null=True, blank=True)  # Duration in seconds
    weight = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  # Weight in kilograms
    distance = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  # Distance in kilometers
    intensity = models.CharField(max_length=100, null=True, blank=True)  # Intensity level or heart rate
    notes = models.TextField(null=True, blank=True)  # Additional notes or comments

    def __str__(self):
        return self.title

class ExerciseLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    date = models.DateField()
    sets = models.PositiveIntegerField(default=1)
    repetitions = models.PositiveIntegerField(default=1)
    duration = models.DurationField(null=True, blank=True)
    weight = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    distance = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    intensity = models.CharField(max_length=100, null=True, blank=True)
    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.exercise.title} - {self.date}"
