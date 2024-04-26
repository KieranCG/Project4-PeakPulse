from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)
    friendly_name = models.CharField(max_length=100, null=True, blank=True, default="")

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Exercise(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    body_part = models.CharField(max_length=100)
    equipment = models.CharField(max_length=100)
    level = models.CharField(max_length=100)
    rating = models.FloatField(blank=True, null=True)
    rating_desc = models.CharField(max_length=255, blank=True)

    # ForeignKey relationship
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
