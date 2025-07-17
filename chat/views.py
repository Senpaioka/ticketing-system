from django.shortcuts import render

# Create your views here.

# def chat_room_page(request, room_name):

#     html_template_name = 'chat/chat.html'

#     context = {}
    
#     return render(request, html_template_name, context)



def index(request):
    return render(request, "chat/chat.html")


def room(request, room_name):
    return render(request, "chat/room.html", {"room_name": room_name})