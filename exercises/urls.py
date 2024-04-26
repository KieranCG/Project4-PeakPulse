from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_exercises, name='exercises'),
    path('<int:exercise_id>', views.exercise_detail, name='exercise_detail'),
]
