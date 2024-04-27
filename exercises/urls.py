from django.urls import path
from . import views
from .views import exercise_log_detail

urlpatterns = [
    path('', views.all_exercises, name='exercises'),
    path('<int:exercise_id>', views.exercise_detail, name='exercise_detail'),
    path('logs/', views.all_exercise_logs, name='exercise_logs'),
    path('logs/<int:exercise_log_id>/', views.exercise_log_detail, name='exercise_log_detail'),  # New URL for exercise log detail view
    path('create/', views.create_exercise_log, name='create_exercise_log'),
]
