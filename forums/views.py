from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import *
from django.views.generic import DeleteView
from django.urls import reverse_lazy


# Create your views here.
def write_topic(request):
    form = WriteTopic()
    writer = request.user.profile

    if request.method == 'POST':
        form = WriteTopic(request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.writer = writer
            new_topic.save()
            messages.success(request, 'Topic was written')
            return redirect('forum')
        else:
            messages.error(request, 'Bad form input')
    return render(request, 'write_topic.html', {'form': form})


def write_comment(request, pk):
    the_topic = Topics.objects.get(id=pk)
    writer = request.user.profile
    form = WriteComment()

    if request.method == 'POST':
        form = WriteComment(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.writer = writer
            new_comment.topic = the_topic
            new_comment.save()
            messages.success(request, 'Comment was written')
            return redirect('forum')
        else:
            messages.error(request, 'Bad form input')
    return render(request, 'write_comment.html', {'form': form})


def forum(request):
    topics = Topics.objects.all().order_by('-date_written')
    return render(request, 'forum.html', {"data": topics})


def spec_topic(request, pk):
    topic = Topics.objects.get(id=pk)
    comments = Comments.objects.filter(topic=topic).order_by('-date_written')
    return render(request, 'spec_topic.html', {"topic": topic, 'comments': comments})


class DeleteTopic(DeleteView):
    model = Topics
    success_url = reverse_lazy('forum')
    template_name = 'topic_delete_confirm.html'

class DeleteComment(DeleteView):
    model = Comments
    success_url = reverse_lazy('forum')
    template_name = 'comment_delete_confirm.html'
