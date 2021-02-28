from django.urls import path, include
from .views import login_view, register_view, logout_view

urlpatterns = [
    path('login/', login_view),
    path('register/', register_view),
    path('logout/', logout_view)
]
