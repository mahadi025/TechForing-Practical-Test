from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/', views.TaskRetrieveUpdateDestroyView.as_view(), name='task-detail'),
    path('<int:task_id>/comments/', views.CommentListCreateView.as_view(), name='comment-list-create')
]