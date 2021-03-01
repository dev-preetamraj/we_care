from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, get_user_model, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import Group

from .forms import UserRegisterForm, UpdateProfileForm, UserUpdateForm
from .models import Profile

# Create your views here.


@unauthenticated_user
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username or Password is incorrect')
    context = {}
    return render(request, 'accounts/login.html', context)


@unauthenticated_user
def register_view(request):
    form = UserRegisterForm()
    # role_form = RoleRegister()

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user_save = form.save()
            if form.cleaned_data.get('is_doctor') == 'YES':
                set_group = Group.objects.get(name='doctor')
                user_save.groups.add(set_group)
            else:
                set_group = Group.objects.get(name='commonUser')
                user_save.groups.add(set_group)

            return redirect('login')
    context = {
        'form': form,
    }
    return render(request, 'accounts/register.html', context)


def logout_view(request):
    logout(request)
    return redirect('home')


@login_required
def ProfileView(request):
    profile = request.user.profile
    form = UpdateProfileForm(instance=profile)
    if request.method == 'POST':
        form = UpdateProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()

    context = {
        'form': form
    }
    return render(request, 'profile/profile.html', context)


@login_required
def ProfileUpdateView(request):
    return render(request, 'profile/test.html', {})
