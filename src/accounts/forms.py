from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, get_user_model
from .models import Profile

User = get_user_model()


class UserRegisterForm(UserCreationForm):
    CHOICES = [
        ('YES', 'Yes'),
        ('NO', 'No')
    ]
    is_doctor = forms.ChoiceField(choices=CHOICES)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1',
                  'password2', 'first_name', 'last_name', 'is_doctor']


class UserUpdateForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']


class UpdateProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['homeaddress', 'country', 'experience',
                  'specialization', 'age', 'about', 'profile_pic']
