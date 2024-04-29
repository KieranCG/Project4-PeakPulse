from django import forms
from .models import Post, Testimonial


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['content']


class TestimonialForm(forms.ModelForm):
    class Meta:
        model = Testimonial
        fields = ['content']
