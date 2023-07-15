from django.shortcuts import render
from .models import Message

# Create your views here.
def home(request):
    return render(request, 'core/index.html')

def direct_messages(request, username):
    """"""
    user = request.user
    r_messages = Message.get_message(user=user) # Returns a list of users that a sender has sent messages before and the date at which the last message was sent to each recipient
    direct_messages = Message.objects.filter(
       user=user,
       recipient__username= username,
    ) # Returns 'Message' instances that a sender has sent to a particular recipient
    for r_msg in r_messages:
        if r_msg['recipient'] == username: # checks if the msg recipient equals to the recipient passed as an argument
            r_msg['unread'] = 0 # sets the unread messages count to 0

    context = {
        'r_messages': r_messages,
        'direct_messages': direct_messages,
        'currnt_username': username
    }
    return render(request, 'core/index.html', context)