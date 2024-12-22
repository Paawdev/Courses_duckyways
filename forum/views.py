from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Topic, Reply
from .forms import TopicForm, ReplyForm

def forum_home(request):
    topics = Topic.objects.all().order_by('-created_at')
    return render(request, 'forum/home.html', {'topics': topics})

@login_required
def create_topic(request):
    if request.method == "POST":
        form = TopicForm(request.POST)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.creator = request.user
            topic.save()
            return redirect('forum_home')
    else:
        form = TopicForm()
    return render(request, 'forum/create_topic.html', {'form': form})

def topic_detail(request, pk):
    topic = get_object_or_404(Topic, pk=pk)
    replies = topic.replies.all().order_by('created_at')
    if request.method == "POST":
        form = ReplyForm(request.POST)
        if form.is_valid():
            reply = form.save(commit=False)
            reply.creator = request.user
            reply.topic = topic
            reply.save()
            return redirect('topic_detail', pk=pk)
    else:
        form = ReplyForm()
    return render(request, 'forum/topic_detail.html', {'topic': topic, 'replies': replies, 'form': form})
