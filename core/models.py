from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Message(models.Model):
    user =          models.ForeignKey(User, on_delete=models.CASCADE)
    sender =        models.ForeignKey(User, on_delete=models.CASCADE, related_name='from_user')
    receipient =    models.ForeignKey(User, on_delete=models.CASCADE, related_name='to_user')
    body =          models.TextField(null=True)
    date =          models.DateTimeField(auto_now_add=True)
    is_read =       models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username}'s message"
    
    def sender_message(self, from_user, to_user, body):
        sender_message = Message(
            user = from_user,
            sender = from_user,
            receipient = to_user,
            body = body,
            is_read = True
        )
        sender_message.save()

        receipient_message = Message(
            user = from_user,
            sender = from_user,
            recepient = to_user,
            body = body,
            is_read = True
        )
        receipient_message.save()

        return sender_message