from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/', views.CommentRetrieveUpdateDestroyView.as_view(), name='comment-detail')
]