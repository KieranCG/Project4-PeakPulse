from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_exercises, name='exercises'),
    path('<int:exercise_id>', views.exercise_detail, name='exercise_detail'),
    path('logs/', views.all_exercise_logs, name='exercise_logs'),  # URL for displaying all exercise logs
    path('create/', views.create_exercise_log, name='create_exercise_log'),
]
