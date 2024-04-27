from django.contrib import admin
from .models import Exercise, ExerciseCategory, ExerciseLog


class ExerciseAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'rating',
        'category',
        'bodypart',
        'level',
    )
    ordering = ('category',)


class ExerciseCategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


class ExerciseLogAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'exercise',
        'date',
        'sets',
        'repetitions',
        'duration',
        'weight',
        'distance',
        'intensity',
        'notes',
    )


admin.site.register(Exercise, ExerciseAdmin)
admin.site.register(ExerciseCategory, ExerciseCategoryAdmin)
admin.site.register(ExerciseLog, ExerciseLogAdmin)
