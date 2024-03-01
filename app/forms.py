from django import forms 
from app.models import *

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','password','email']
        widgets = {
            'username':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Username'}),
            'password':forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter Password'}),
            'email':forms.EmailInput(attrs={'class':'form-control','placeholder':'Enter Email'}),
        }
        help_texts = {'username':''}

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['address','profile_pic']
        widgets = {
            'address':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Address'}),
            'profile_pic':forms.ClearableFileInput(attrs={'class':'form-control'})
        }
