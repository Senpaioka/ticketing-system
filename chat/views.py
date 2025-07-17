from django.shortcuts import render, redirect
from utils.room_generator import generate_random_id
from django.urls import reverse

def index(request):
    
    room_id = generate_random_id()
    return redirect(reverse('chat:room', kwargs={'room_name': room_id}))



def room(request, room_name):

    html_template_name = 'chat/room.html'

    context = {
        "room_name": room_name,
        }

    return render(request, html_template_name, context)