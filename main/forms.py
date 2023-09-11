from django import forms
from .models import Callback

class CallbackForm(forms.ModelForm):
    name = forms.CharField(max_length=50, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': "Name "
        }
    ))
    phone = forms.CharField(max_length=50, widget=forms.TextInput(
        attrs={'class': 'form-control',
               'placeholder': "Phone"
               }
    ))
    email = forms.EmailField(max_length=50, widget=forms.EmailInput(
        attrs={'class': 'form-control',
               'placeholder': "Email"
               }
    ))
    message = forms.CharField(max_length=50, widget=forms.TextInput(
        attrs={'class': 'form-control',
               'placeholder': "Message"
               }
    ))

    class Meta:
        model = Callback
        fields = ['name', 'phone', 'email', 'message']
