from django.shortcuts import render, redirect, get_object_or_404
from ticket.form import TicketForm, UpdateTicketForm, CommentForm
from ticket.models import createTicket, CommentModel
from account.models import UserAccount

# Create your views here.
def creating_ticket(request, username):
    
    html_template_name = 'ticket/open.html'
    
    get_user = UserAccount.objects.get(username=username)

    if request.method == 'POST':
        ticket_form = TicketForm(request.POST, request.FILES)

        if ticket_form.is_valid():
            title = ticket_form.cleaned_data['title']
            description = ticket_form.cleaned_data['description']
            category = ticket_form.cleaned_data['category']
            priority = ticket_form.cleaned_data['priority']
            uploaded_file = None

            if ticket_form.cleaned_data['uploaded_file']:
                uploaded_file = ticket_form.cleaned_data['uploaded_file']
        
        

            ticket = createTicket.objects.create(
                title = title,
                description = description,
                category = category,
                priority = priority,
                uploaded_file = uploaded_file
            )
            ticket.user_account = get_user      
            ticket.save()

        return redirect('ticket:success')

    else:
        ticket_form = TicketForm()


    context = {
        'form': ticket_form,
    }

    return render(request, html_template_name, context)





def update_ticket(request, ticket_id):

    html_template_name = 'ticket/edit.html'

    get_ticket_id = ticket_id
    get_ticket = get_object_or_404(createTicket, pk=ticket_id)
    edit_form = UpdateTicketForm(instance=get_ticket) 

    if request.method == 'POST':
            
        edit_form = UpdateTicketForm(request.POST, request.FILES, instance=get_ticket)

        if edit_form.is_valid():
            update_form = edit_form.save(commit=False)
            update_form.save()

            return redirect('ticket:updated')

        else:
            edit_form = UpdateTicketForm(instance=get_ticket) 

    context = {
        'form': edit_form,
        'id_ticket': get_ticket_id,
    }

    return render(request, html_template_name, context)





def update_success(request):

    html_template_name = 'ticket/updated.html'
    context = {}
    return render(request, html_template_name, context)





def ticket_page(request, username):

    html_template_name = 'ticket/ticket.html'

    get_tickets = createTicket.objects.filter(user_account__username=username).all()

    context = {
        'ticket_info': get_tickets,
    }

    return render(request, html_template_name, context)






def delete_ticket(request, ticket_id):

    get_ticket = createTicket.objects.get(pk=ticket_id)
    get_ticket.delete()

    return redirect('home:home')
    





def success_page(request):

    html_template_name = 'ticket/success.html'

    context = {}

    return render(request, html_template_name, context) 






def comment_page(request, ticket_id):

    html_template_name = 'ticket/comment.html'

    ticket_value = ticket_id

    get_comment = CommentModel.objects.filter(ticket_no=ticket_id)

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)

        if comment_form.is_valid():
            comment = comment_form.cleaned_data['message']

            save_comment = CommentModel.objects.create(
                user_info = request.user,
                ticket_no = ticket_id,
                message = comment,
            )

            comment_form = CommentForm()

            save_comment.save()

    else:
        comment_form = CommentForm()

    context = {
        'form': comment_form,
        'id_ticket': ticket_value,
        'comments' : get_comment,
    }

    return render(request, html_template_name, context)




def admin_ticket_page(request):

    html_template_name = 'ticket/all.html'

    all_tickets = createTicket.objects.all()

    context = {
        'ticket_info': all_tickets,
    }

    return render(request, html_template_name, context)


