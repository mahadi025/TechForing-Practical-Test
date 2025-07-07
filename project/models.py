from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=254, unique=True)
    description = models.TextField(blank=True)
    owner = models.ForeignKey('user.User', on_delete=models.CASCADE, related_name='project')
    created_at = models.DateTimeField(auto_now_add=True)

class ProjectMember(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='members')
    user = models.ForeignKey('user.User', on_delete=models.CASCADE, related_name='project_member')
    role = models.CharField(max_length=15, choices=[('admin', 'Admin'), ('member', 'Member')], default='member')