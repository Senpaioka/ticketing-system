from django.urls import path
from account import views


app_name = 'account'

urlpatterns = [
    path('login/', views.login_page, name='login'),
    path('registration/', views.registration_page, name='register'),
    path('logout/', views.logout_view, name='logout'),
]