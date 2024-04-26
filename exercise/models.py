from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)
    friendly_name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Exercise(models.Model):
    exercise_id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    type = models.CharField(max_length=100)
    body_part = models.CharField(max_length=100)
    equipment = models.CharField(max_length=100)
    level = models.CharField(max_length=100)
    rating = models.FloatField(blank=True, null=True)
    rating_desc = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.title
