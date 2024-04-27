from django.core.paginator import Paginator, EmptyPage
from django.shortcuts import render, get_object_or_404
from django.db.models.functions import Lower
from .models import Exercise, ExerciseLog
from django.db.models import F, Q
from .forms import ExerciseLogForm
from django.contrib.auth.decorators import login_required


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


def all_exercise_logs(request):
    """ A view to show all exercise logs, including sorting and search queries """

    # Fetch the single exercise log
    exercise_log = ExerciseLog.objects.all()
    context = {
        'exercise_log': exercise_log,
    }

    return render(request, 'exercises/exercise_logs.html', context)


def exercise_log_detail(request, exercise_log_id):
    """ A view to show details of a single exercise log """
    exercise_log = get_object_or_404(ExerciseLog, pk=exercise_log_id)

    context = {
        'exercise_log': exercise_log,
    }

    return render(request, 'exercises/exercise_log_detail.html', context)


@login_required
def create_exercise_log(request):
    if request.method == 'POST':
        form = ExerciseLogForm(request.POST)
        if form.is_valid():
            # If the form is valid, save the data and redirect
            exercise_log = form.save(commit=False)
            exercise_log.user = request.user
            exercise_log.save()
            return redirect('exercise_logs')
    else:
        form = ExerciseLogForm()
    return render(request, 'exercises/exercise_log_form.html', {'form': form})
