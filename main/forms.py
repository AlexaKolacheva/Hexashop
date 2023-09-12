from django import forms
from .models import Callback, Review, Feedback, Comment

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


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['author', 'content']

class FeedbackForm(forms.Form):
    class Meta:
        model = Feedback
        fields = ['name', 'text', 'gender', 'profession']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['author', 'text']
