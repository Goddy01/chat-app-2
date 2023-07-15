from django.db import models
from django.db.models import Count, Max, Sum
from django.contrib.auth.models import User

# Create your models here.
class Message(models.Model):
    user =          models.ForeignKey(User, on_delete=models.CASCADE)
    sender =        models.ForeignKey(User, on_delete=models.CASCADE, related_name='from_user')
    recipient =     models.ForeignKey(User, on_delete=models.CASCADE, related_name='to_user')
    body =          models.TextField(null=True)
    date =          models.DateTimeField(auto_now_add=True)
    is_read =       models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username}'s message"
    
    def sender_message(self, from_user, to_user, body):
        sender_message = Message(
            user = from_user,
            sender = from_user,
            recipient = to_user,
            body = body,
            is_read = True
        )
        sender_message.save()

        recipient_message = Message(
            user = from_user,
            sender = from_user,
            recepient = to_user,
            body = body,
            is_read = True
        )
        recipient_message.save()

        return sender_message
    
    def get_message(user):
        recipients = []

        # Retrieves all the messages sent by the user to other users while annotating 'last' and ordering the retrieved queryset by the most recent message (descending)
        messages = Message.objects.filter(user=user).values('recipient').annotate(last=Max('date')).order_by('-last')
        # messages2= Message.objects.filter(user=user).values('recipient').order_by('-sent_at')
        for msg in messages:
            username = User.objects.get(pk=msg['recipient']).username
            recipients.append({
                'user': User.objects.get(username=username),
                'last': msg['last'],
                'unread': Message.objects.filter(user=user, recipient__pk=msg['recipient'], is_read=False).count()
            })
        return recipients