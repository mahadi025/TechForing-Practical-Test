from django.db import models

class Comment(models.Model):
    content = models.TextField(blank=True)
    user = models.ForeignKey('user.User', on_delete=models.CASCADE, related_name='comment')
    task = models.ForeignKey('task.Task', on_delete=models.CASCADE, related_name='comment')
    created_at = models.DateTimeField(auto_now_add=True)
