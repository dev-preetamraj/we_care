from django.urls import path, include
from .views import login_view, register_view, logout_view, ProfileView, ProfileUpdateView

urlpatterns = [
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('logout/', logout_view, name='logout'),
    path('update_profile/', ProfileUpdateView, name='update_profile'),
    path('profile/', ProfileView, name='profile')
]
