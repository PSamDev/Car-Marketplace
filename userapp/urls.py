from django.urls import path
from . import views
from .views import ProfileView, Register

urlpatterns = [
    path("login/", views.login_view, name="login"),
    path("register/", Register.as_view(), name="register"),
    path("logout/", views.logout_view, name="logout"),
    path("profile/", ProfileView.as_view(), name="profile")
]
