from django.shortcuts import render
from .models import Message
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def home_chat(request):
    user = request.user
    messages = Message.get_message(user=user)
    lastest_msg_username = None
    associated_msgs = None
    if messages:
        message = messages[0]
        lastest_msg_username = message['user'].username
        associated_msgs = Message.objects.filter(user=user, recipient__username=lastest_msg_username)
        message.update(is_read=True)
        
        for msg in messages:
            if msg['user'].username == lastest_msg_username:
                msg['unread'] = 0
    return render(request, 'core/index.html')


@login_required
def direct_messages(request, username):
    """"""
    user = request.user
    r_messages = Message.get_message(user=user) # Returns a list of users that a sender has sent messages before and the date at which the last message was sent to each recipient
    direct_messages = Message.objects.filter(
       user=user,
       recipient__username= username,
    ) # Returns 'Message' instances that a sender has sent to a particular recipient
    direct_messages.update(is_read=True)
    for r_msg in r_messages:
        if r_msg['recipient'] == username: # checks if the msg recipient equals to the recipient passed as an argument
            r_msg['unread'] = 0 # sets the unread messages count to 0

    context = {
        'r_messages': r_messages,
        'direct_messages': direct_messages,
        'currnt_username': username,
        'user': user
    }
    return render(request, 'core/index.html', context)