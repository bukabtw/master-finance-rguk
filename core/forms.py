from django import forms
from .models import Application

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ('name', 'phone', 'email', 'message')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Ваше имя'}),
            'phone': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Ваш телефон'}),
            'email': forms.EmailInput(attrs={'class': 'form-input', 'placeholder': 'Ваш email'}),
            'message': forms.Textarea(attrs={'class': 'form-input', 'placeholder': 'Ваше сообщение', 'rows': 4}),
        }
