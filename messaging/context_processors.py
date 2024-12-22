from .models import Message

def unread_messages_count(request):
    if request.user.is_authenticated:
        unread_count = Message.objects.filter(recipient=request.user, is_read=False, is_active=True).count()
    else:
        unread_count = 0
    return {'unread_messages_count': unread_count}
