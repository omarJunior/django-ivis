from django.urls import path
from . import views

urlpatterns = [
    path('', views.profiles, name="profiles"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.registerUser, name="register"),
    path('profile/<str:pk>/', views.userProfile, name="user_profile"),
    path('account/', views.userAccount, name="account"),
    path('edit-account/', views.editAccount, name="edit_account"),
    path('create-skill/', views.createSkill, name="create_skill"),
    path('update-skill/<str:pk>/', views.updateSkill, name="update_skill"),
    path('delete-skill/<str:pk>/', views.deleteSkill, name="delete_skill"),
    path('inbox/', views.inbox, name="inbox"),
    path('message/<str:pk>/', views.viewMessage, name="message"),
    path('create-message/<str:pk>/', views.createMessage, name="create_message"),
]