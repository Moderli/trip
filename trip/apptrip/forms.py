# myapp/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(
        max_length=254,
        help_text='Required. Enter a valid email address.'
    )
    
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        min_length=15,
        help_text="Your password must contain at least 15 characters."
    )

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2', 'first_name', 'last_name')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError('This email address is already in use.')
        return email
