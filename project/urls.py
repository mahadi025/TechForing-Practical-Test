from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProjectListCreateView.as_view(), name='project-list-create'),
    path('<int:pk>/', views.ProjectRetrieveUpdateDestroyView.as_view(), name='project-detail'),
    path('<int:project_id>/tasks/', views.TaskListCreateView.as_view(), name='task-list-create')
]