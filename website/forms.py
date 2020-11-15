from django import forms

from .models import Contact


class ContactForm(forms.ModelForm):


    nom = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'yan_input',
        'placeholder': 'Votre nom',
    }))

    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': 'yan_input',
        'placeholder': 'Email',
    }))

    message = forms.CharField(widget=forms.Textarea(attrs={
        'placeholder': 'Message',
        'cols': '30',
        'rows': '10',
    }))


    class Meta:
        model = Contact
        fields = ['nom', 'email', 'message']