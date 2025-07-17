from django.urls import path
from ticket import views


app_name = 'ticket'

urlpatterns = [
    path('create/<str:username>/', views.creating_ticket, name='create_ticket'),
    path('ticket_list/<str:username>/', views.ticket_page, name='ticket_page'),
    path('edit_ticket/<str:ticket_id>/', views.update_ticket, name='ticket_update'),
    path('delete/<str:ticket_id>/', views.delete_ticket, name='delete'),
    path('success/', views.success_page, name='success'),
    path('updated/', views.update_success, name='updated'),
    path('comments/<int:ticket_id>/', views.comment_page, name='comment'),
    path('admin_action/', views.admin_ticket_page, name='admin_ticket'),
]