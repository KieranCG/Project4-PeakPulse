from django.urls import path
from . import views

app_name = 'community'

urlpatterns = [
    path('', views.community_view, name='community'),
    path('add-post/', views.add_post, name='add_post'),
    path('testimonials/', views.testimonials_view, name='testimonials'),
]
