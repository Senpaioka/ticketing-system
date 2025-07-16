from django import forms
from account.models import UserAccount



class RegistrationForm(forms.ModelForm):

    password = forms.CharField(label="password", widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter Password',
    }))

    confirm_password = forms.CharField(label="confirm_password", widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Password confirmation'
    }))

    class Meta:
        model = UserAccount
        fields = ['full_name', 'username', 'email']
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Full Name'}),
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
        }


    def clean(self):

        cleaned_data = super(RegistrationForm, self).clean()

        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:

            raise forms.ValidationError (
                "Password does not match!"
            )