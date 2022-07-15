from django.db import models
from groups.models import Group
from django.urls import reverse
from django.conf import settings
from django.contrib.auth import get_user_model
# Create your models here.

User = get_user_model()

class Post(models.Model):
    title = models.CharField(max_length=128, unique = True)
    user = models.ForeignKey(User, related_name="posts", on_delete=models.CASCADE)
    createTime = models.DateTimeField(auto_now=True)
    group = models.ForeignKey(Group, related_name='posts', on_delete=models.CASCADE)
    content = models.TextField(max_length=512)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('posts:post-detail', kwargs={'post_pk':self.pk})

    class Meta:
        ordering = ['-createTime']
        unique_together = ('user', 'title', 'content')