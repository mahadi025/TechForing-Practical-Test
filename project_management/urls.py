from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/', include('user.urls')),
    path('api/projects/', include('project.urls')),
    path('api/tasks/', include('task.urls')),
    path('api/comments/', include('comment.urls'))
]
