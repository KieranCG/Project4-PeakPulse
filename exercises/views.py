from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from .models import Exercise


def all_exercises(request):
    """ A view to show all exercises, including sorting and search queries """

    exercises_list = Exercise.objects.all()

    # Number of exercises to display per page
    items_per_page = 20  # Change this to 20 for 20 items per page

    # Initialize Paginator object with queryset and items per page
    paginator = Paginator(exercises_list, items_per_page)

    # Get the current page number from the request, default to page 1
    page_number = request.GET.get('page', 1)

    try:
        # Get the page object for the requested page number
        page_obj = paginator.page(page_number)
    except EmptyPage:
        # If the requested page is out of range, deliver last page of results
        page_obj = paginator.page(paginator.num_pages)

    context = {
        'page_obj': page_obj,
    }

    return render(request, 'exercises/exercises.html', context)


def exercise_detail(request, exercise_id):
    """ A view to show individual exercise details """

    exercise = get_object_or_404(Exercise, pk=exercise_id)

    context = {
        'exercise': exercise,
    }

    return render(request, 'exercises/exercises_detail.html', context)
