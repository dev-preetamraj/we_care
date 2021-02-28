from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, get_user_model, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required


from .forms import UserRegisterForm

# Create your views here.


def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
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


def register_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = UserRegisterForm()

        if request.method == 'POST':
            form = UserRegisterForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('login')
        context = {
            'form': form,
        }
        return render(request, 'accounts/register.html', context)


def logout_view(request):
    logout(request)
    return redirect('login')
