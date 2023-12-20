from django.urls import path
from . import views

urlpatterns = [
    path("", views.welcome, name="welcome"),
    path("home/", views.home, name="home"),
    path("list/", views.list_form, name="list_form"),
    path("carinfo/<str:id>", views.carinfo, name="carinfo"),
    path("carinfo/<str:id>/edit/", views.edit, name="edit"),
    path('listing/<str:id>/like/', views.like_listing_view, name='like_listing'),
]
