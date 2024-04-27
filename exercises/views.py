from django.core.paginator import Paginator, EmptyPage
from django.shortcuts import render, get_object_or_404
from django.db.models.functions import Lower
from .models import Exercise
from django.db.models import F, Q


def all_exercises(request):
    """ A view to show all exercises, including sorting and search queries """

    exercises_list = Exercise.objects.all()

    # Sorting
    sort = request.GET.get('sort')
    sortkey = 'title'  # Default sort key
    if sort == 'title':
        sortkey = 'title'
    elif sort == 'rating':
        sortkey = 'rating'
    # Add other sorting options as needed

    direction = request.GET.get('direction')
    if direction == 'desc':
        sortkey = f'-{sortkey}'

    if sort == 'title':
        # Use lower_title for case-insensitive sorting by title
        exercises_list = exercises_list.annotate(lower_title=Lower('title')).order_by(sortkey)
    else:
        exercises_list = exercises_list.order_by(sortkey)

    # Searching
    search_term = request.GET.get('q')
    if search_term:
        queries = Q(title__icontains=search_term) | Q(description__icontains=search_term)
        exercises_list = exercises_list.filter(queries)

    # Pagination
    items_per_page = 20  # Change this to the desired number of items per page
    paginator = Paginator(exercises_list, items_per_page)
    page_number = request.GET.get('page', 1)

    try:
        page_obj = paginator.page(page_number)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)

    context = {
        'page_obj': page_obj,
        'search_term': search_term,
    }

    return render(request, 'exercises/exercises.html', context)


def exercise_detail(request, exercise_id):
    """ A view to show individual exercise details """

    exercise = get_object_or_404(Exercise, pk=exercise_id)

    context = {
        'exercise': exercise,
    }

    return render(request, 'exercises/exercises_detail.html', context)
