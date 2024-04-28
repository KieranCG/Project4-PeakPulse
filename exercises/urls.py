from django.urls import path
from . import views
from .views import exercise_log_detail

urlpatterns = [
    path('', views.all_exercises, name='exercises'),
    path('<int:exercise_id>', views.exercise_detail, name='exercise_detail'),
    path('logs/', views.all_exercise_logs, name='exercise_logs'),
    path('logs/<int:exercise_log_id>/', views.exercise_log_detail, name='exercise_log_detail'),
    path('add-exercise-log/', views.add_exercise_log, name='add_exercise_log'),
    path('edit-exercise-log/<int:log_id>/', views.edit_exercise_log, name='edit_exercise_log'),
]
