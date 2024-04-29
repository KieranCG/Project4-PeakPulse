from django.shortcuts import render, redirect
from .models import Post, Testimonial
from .forms import PostForm, TestimonialForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def community_view(request):
    """ A view to show all posts, including sorting """
    posts = Post.objects.all()
    return render(request, 'community/community.html', {'posts': posts})


@login_required
def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            # Save the post
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            # Add a success message
            messages.success(request, 'Post added successfully!')
            # Redirect to the community page
            return redirect('community:community')
        else:
            # Add an error message if the form is not valid
            messages.error(request, 'Failed to add post. Please check the form.')
    else:
        form = PostForm()
    return render(request, 'community/add_post.html', {'form': form})


def testimonials_view(request):
    """ A view to display testimonials """
    testimonials = Testimonial.objects.all().order_by('-created_at')
    return render(request, 'community/testimonials.html', {'testimonials': testimonials})


@login_required
def add_testimonial(request):
    if request.method == 'POST':
        form = TestimonialForm(request.POST)
        if form.is_valid():
            # Save the testimonial
            testimonial = form.save(commit=False)
            testimonial.user = request.user
            testimonial.save()
            # Add a success message
            messages.success(request, 'Testimonial added successfully!')
            # Redirect to the testimonials page
            return redirect('community:testimonials')
        else:
            # Add an error message if the form is not valid
            messages.error(request, 'Failed to add testimonial. Please check the form.')
    else:
        form = TestimonialForm()
    return render(request, 'community/add_testimonial.html', {'form': form})
