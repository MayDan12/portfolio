from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile



class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    # bio = forms.Textarea()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    bio = forms.Textarea()
    class Meta:
        model = UserProfile
        fields = ['profile_picture', 'bio']



