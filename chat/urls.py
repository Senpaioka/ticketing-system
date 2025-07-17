from django.urls import path
from chat import views

app_name = 'chat'

urlpatterns = [
    path("create_room/", views.index, name="index"),
    path("<str:room_name>/", views.room, name="room"),
]
