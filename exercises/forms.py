from django import forms
from .models import ExerciseLog


class ExerciseLogForm(forms.ModelForm):
    class Meta:
        model = ExerciseLog
        exclude = ('user',)  # Exclude the user field as it will be set automatically

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'exercise': 'Exercise Name',
            'date': 'Date (YYYY-MM-DD)',
            'sets': 'Sets',
            'repetitions': 'Repetitions',
            'duration': 'Duration (in seconds)',
            'weight': 'Weight (in kilograms)',
            'distance': 'Distance (in kilometers)',
            'intensity': 'Intensity',
            'notes': 'Notes',
        }

        self.fields['exercise'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'date':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = ('border-black '
                                                        'rounded-0 '
                                                        'exercise-log-form-input')
            self.fields[field].label = False
