from django.contrib import admin
from .models import Exercise


class ExerciseAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'body_part',
        'equipment',
        'level',
        'rating',
    )

    ordering = ('title',)


admin.site.register(Exercise, ExerciseAdmin)
