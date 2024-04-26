from django.db import models


class ExerciseCategory(models.Model):
    name = models.CharField(max_length=100)
    friendly_name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Exercise(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    bodypart = models.CharField(max_length=100)
    equipment = models.CharField(max_length=100)
    level = models.CharField(max_length=100)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    ratingdesc = models.CharField(max_length=200)
    category = models.ForeignKey(ExerciseCategory, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.title
