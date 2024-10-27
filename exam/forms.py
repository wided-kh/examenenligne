from django import forms
from django.contrib.auth.models import User
from . import models

from django import forms

class ContactusForm(forms.Form):
    Name = forms.CharField(
        max_length=30,
        label='Your Name',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your name',
            'required': 'required'  # Add 'required' attribute for HTML validation
        })
    )
    
    Email = forms.EmailField(
        label='Your Email',
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your email',
            'required': 'required'  # Add 'required' attribute for HTML validation
        })
    )
    
    Message = forms.CharField(
        max_length=500,
        label='Your Message',
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 5,
            'placeholder': 'Type your message here',
            'required': 'required'  # Add 'required' attribute for HTML validation
        })
    )



