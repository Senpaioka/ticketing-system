from django.shortcuts import render, redirect
import random
import string
from django.urls import reverse

def generate_random_id(length=12):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))


def index(request):
    
    random_room = generate_random_id()
    return redirect(reverse('chat:room', kwargs={'room_name': random_room}))



def room(request, room_name):

    html_template_name = 'chat/room.html'

    context = {
        "room_name": room_name,
        }

    return render(request, html_template_name, context)