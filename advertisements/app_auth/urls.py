from django.contrib.auth import logout
from django.urls import path

from .views import profile_view, login_view, logout_view, register_view

urlpatterns = [
    path("login/", login_view, name='login'),
    path("profile/", profile_view, name="profile"),
    path("logout/", logout, name='logout'),
    # TODO(logout на logout_view)
    path('register/', register_view, name='register'),

]
