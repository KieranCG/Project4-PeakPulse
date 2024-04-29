from django.contrib import admin
from .models import Post, Comment, Testimonial


class PostAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'content',
        'created_at',
    )


class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'post',
        'content',
        'created_at',
    )


class TestimonialAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'content',
        'created_at',
    )


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Testimonial, TestimonialAdmin)
