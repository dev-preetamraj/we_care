from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from accounts.decorators import allowed_users
from django.contrib.auth.models import User
# Create your views here.


# @allowed_users(allowed_roles=['doctor'])
def index(request):
    current_user = request.user
    queryset = User.objects.filter(groups__name='doctor')
    # group = request.user.groups.all()[0].name
    context = {'user': current_user, 'queryset': queryset}
    return render(request, 'main/base.html', context)


def user_profile(request):
    # id = pk
    group = request.user.groups.all()[0].name
    context = {'group': group}
    return render(request, 'profile/profile.html', context)
