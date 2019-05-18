from django import forms

class ImageForm(forms.ModelForm):
    your_name = forms.CharField(label='First Name',max_length=30)
    email = forms.EmailField(label='Email')