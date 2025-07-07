from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=254)
    description = models.TextField(blank=True)
    status = models.CharField(max_length=15, choices=[('todo', 'To Do'), ('in_progress', 'In Progress'), ('done', 'Done')], default='todo')
    priority = models.CharField(max_length=15, choices=[('low', 'Low'), ('medium', 'Medium'), ('high', 'High')], default='medium')
    assgned_to = models.ForeignKey('user.User', on_delete=models.CASCADE, related_name='task', null=True, blank=True)
    project = models.ForeignKey('project.Project', on_delete=models.CASCADE, related_name='task')
    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(null=True, blank=True)