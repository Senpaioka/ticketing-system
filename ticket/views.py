from django.shortcuts import render

# Create your views here.
def creating_ticket(request):
    
    html_template_name = 'ticket/open.html'

    context = {}

    return render(request, html_template_name, context)