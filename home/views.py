from django.shortcuts import render

# Create your views here.
def home_page(request):

    html_template_name = 'home/home.html'
    context = {}
    return render(request, html_template_name, context)
