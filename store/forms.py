from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

class SignUpForm(UserCreationForm):
    email = forms.EmailField(
        label="",
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Email Address',
            'style': 'border: 1px solid #dee2e6; border-radius: 8px; padding: 12px;'
        })
    )
    first_name = forms.CharField(
        label="", 
        max_length=100, 
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'First Name',
            'style': 'border: 1px solid #dee2e6; border-radius: 8px; padding: 12px;'
        })
    )
    last_name = forms.CharField(
        label="", 
        max_length=100, 
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Last Name',
            'style': 'border: 1px solid #dee2e6; border-radius: 8px; padding: 12px;'
        })
    )

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        # Style username field
        self.fields['username'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Username',
            'style': 'border: 1px solid #dee2e6; border-radius: 8px; padding: 12px;'
        })
        self.fields['username'].label = ''
        
        # Style password1 field
        self.fields['password1'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Password',
            'style': 'border: 1px solid #dee2e6; border-radius: 8px; padding: 12px;'
        })
        self.fields['password1'].label = ''
        
        # Style password2 field
        self.fields['password2'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Confirm Password',
            'style': 'border: 1px solid #dee2e6; border-radius: 8px; padding: 12px;'
        })
        self.fields['password2'].label = ''
        
        # Remove help text for cleaner form
        self.fields['username'].help_text = ''
        self.fields['password1'].help_text = ''
        self.fields['password2'].help_text = ''