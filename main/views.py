from django.shortcuts import render, redirect

from products.models import Category
from .models import Callback, Review, Feedback, Comment, About
from .forms import CallbackForm, ReviewForm, FeedbackForm, CommentForm


def callbacks(request):
    if request.method == 'POST':
        form = CallbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = CallbackForm()
    return render(request, 'main/contact.html', {'form': form})



# def feedback(request):
#     feedbacks = Comment.objects.all()
#     context = {
#         'feedbacks': feedbacks
#     }
#     return render(request, 'main/reviews.html', context)


def add_comment(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reviews')
    else:
        form = CommentForm()

    return render(request, 'main/coment.html', {'form': form})


def delete_comment(request, comment_id):
    Comment.objects.filter(id=comment_id).delete()
    return redirect('reviews')


def reviews(request):
    comments = Comment.objects.all()

    context = {
        'comments': comments,
    }

    return render(request, 'main/reviews.html', context)

def about(request):
    abouts = About.objects.all()
    context = {
        'abouts': abouts
    }
    return render(request, 'main/about.html', context)

def index(request):
    categories = Category.objects.all()
    return render(request, 'main/index.html', {'categories': categories})

