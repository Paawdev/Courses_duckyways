from django import forms
from .models import Topic, Reply

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['title']

class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ['content']
