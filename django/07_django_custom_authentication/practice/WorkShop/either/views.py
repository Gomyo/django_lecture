from django.shortcuts import render, redirect, get_object_or_404
from .models import Vote, Comment
from .forms import VoteForm, CommentForm
from django.db.models import Count, Sum
import random

# Create your views here.
def index(request):
    votes = Vote.objects.all()
    context = {
        'votes': votes,
    }
    return render(request, 'either/index.html', context)

def create(request):
    if request.method == 'POST':
        form = VoteForm(request.POST)
        if form.is_valid():
            vote = form.save()
            return redirect('either:detail', vote.pk)
    else:
        form = VoteForm()
    context = {
        'form': form,
    }
    return render(request, 'either/create.html', context)

def detail(request, vote_pk):
    vote = get_object_or_404(Vote, pk=vote_pk)
    comment_form = CommentForm()
    comments = vote.comments.all()
    total = len(vote.comments.all().annotate(Count('pick')))
    if total == 0:
        blue = 0
        red = 0
    else:
        blue = round(comments.filter(pick='BLUE').count() / total * 100, 1)
        red = round(comments.filter(pick='RED').count() / total * 100, 1)
    context = {
        'vote': vote,
        'comments': comments,
        'comment_form': comment_form,
        'total': total,
        'blue': blue,
        'red': red,
    }
    return render(request, 'either/detail.html', context)

def create_comment(request, vote_pk):
    vote = get_object_or_404(Vote, pk=vote_pk)
    comment_form = CommentForm(request.POST)
    if request.method == 'POST':
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.vote = vote
            comment.save()
            return redirect('either:detail', vote.pk)
    context = {
        'comment_form': comment_form,
        'vote': vote,
    }
    return render(request, 'either/detail.html', context)

def random_pick(request):
    votes = Vote.objects.all()
    random_vote = random.choice(votes)
    return redirect('either:detail', random_vote.pk)
