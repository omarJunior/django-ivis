from django.urls import path
from . import views

urlpatterns = [
    path('', views.profiles, name="profile"),
    path('login/', views.loginPage, name="login"),
    path('login/', views.loginPage, name="login"),
    path('register/', views.registerUser, name="register"),
    path('profile/<str:pk>/', views.userProfile, name="user_profile"),
]