from django.urls import path, include
from . import views

urlpatterns = [
    path('projects/', views.projects, name="projects"),
    path('project-object/<str:pk>/', views.project, name="project_object"),
    path('create-project/', views.createProject, name="create_project"),
]