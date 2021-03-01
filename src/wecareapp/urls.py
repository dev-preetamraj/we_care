from django.urls import path
from .views import index, user_profile

urlpatterns = [
    path('', index, name='home'),
    path('profile/', user_profile, name='profile')
]
