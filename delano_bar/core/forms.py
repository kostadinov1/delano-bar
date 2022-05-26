from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(max_length=60, widget=forms.TextInput(attrs={'placeholder': 'Enter Your Name'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Enter Your Email'}))
    message = forms.CharField(max_length=500, widget=forms.Textarea(attrs={'placeholder': 'Enter Message'}))
