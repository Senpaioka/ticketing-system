from django.shortcuts import render, redirect
from account.form import RegistrationForm
from account.models import UserAccount
from django.contrib import auth

# Create your views here.

def registration_page(request):

    html_template_page = 'account/register.html'

    if request.method == 'POST':
        registration_form = RegistrationForm(request.POST)

        if registration_form.is_valid():
            full_name = registration_form.cleaned_data['full_name']
            username = registration_form.cleaned_data['username']
            email = registration_form.cleaned_data['email']
            password = registration_form.cleaned_data['password']    

            # saving all data
            user = UserAccount.objects.create_user(full_name=full_name, username=username, email=email, password=password)
            user.save()

            return redirect('account:login')
        
    else:
        registration_form = RegistrationForm()


    context = {
        'form': registration_form,
    }

    return render(request, html_template_page, context)






def login_page(request):

    html_template_page = 'account/login.html'


    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(request, username=username, password=password)
    
        if user:
            auth.login(request, user)
            return redirect('home:home')
        else:
            print('not found')

    context = {}

    return render(request, html_template_page, context)






def logout_view(request):

    auth.logout(request)
    return redirect('home:home')







