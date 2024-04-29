from django.shortcuts import render
from .models import Post


def community_view(request):
    """ A view to show all posts, including sorting """
    posts = Post.objects.all()
    return render(request, 'community/community.html', {'posts': posts})
