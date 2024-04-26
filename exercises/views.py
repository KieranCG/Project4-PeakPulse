from django.shortcuts import render
from .models import Exercise

# Create your views here.


def all_exercises(request):
    """ A view to show all exercises, including sorting and search queries """

    exercises = Exercise.objects.all()

    context = {
        'exercises': exercises,
    }

    return render(request, 'exercises/exercises.html', context)
