from django.urls import path
from . import views

urlpatterns = [
    path('', views.profiles, name="profile"),
    path('profile/<str:pk>/', views.userProfile, name="user_profile"),
]