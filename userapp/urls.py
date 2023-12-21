from django.urls import path
from . import views
from .views import ProfileView, Register
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("login/", views.login_view, name="login"),
    path("register/", Register.as_view(), name="register"),
    path("logout/", views.logout_view, name="logout"),
    path("profile/", ProfileView.as_view(), name="profile"),
    path('password_reset/',auth_views.PasswordResetView.as_view(),name='password_reset'),
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete')
]
