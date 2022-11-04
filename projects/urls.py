from django.urls import path, include
from . import views

urlpatterns = [
    path('projects/', views.projects, name="projects"),
    path('project-object/<str:pk>/', views.project, name="project"),
    path('create-project/', views.createProject, name="create_project"),
    path('update-project/<str:pk>/', views.updateProject, name="update_project"),
    path('delete-project/<str:pk>/', views.deleteProject, name="delete_project"),
]