from django import forms
from .models import Image,Profile, Comments
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['likes','profile','posted_time','profile']
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        exclude = ['image','user']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']

class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=250, help_text='Required')
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
