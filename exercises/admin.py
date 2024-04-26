from django.contrib import admin
from .models import Exercise, ExerciseCategory


class ExerciseAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'rating',
        'category',
    )

    ordering = ('category',)


class ExerciseCategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Exercise, ExerciseAdmin)
admin.site.register(ExerciseCategory, ExerciseCategoryAdmin)
