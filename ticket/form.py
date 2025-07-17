from django import forms
from ticket.models import createTicket, CommentModel

class TicketForm(forms.ModelForm):

    class Meta:
        model = createTicket
        fields = ['title', 'description', 'category', 'priority', 'uploaded_file']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ticket Subject'}),
            'description': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ticket Description'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'priority': forms.Select(attrs={'class': 'form-control'}),
            
        }



class UpdateTicketForm(forms.ModelForm):

    class Meta:
        model = createTicket
        fields = ['title', 'description', 'category', 'priority', 'uploaded_file']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Update Ticket Subject'}),
            'description': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Update Ticket Description'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'priority': forms.Select(attrs={'class': 'form-control'}),
            'uploaded_file': forms.ClearableFileInput(attrs={'class': 'form-control'}),            
        }




class CommentForm(forms.ModelForm):

    class Meta:
        model = CommentModel
        fields = ['message']
        widgets = {
            'message': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Write something...'}),            
        }
