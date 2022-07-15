from django.contrib import admin
from groups.models import Group
from posts.models import Post
# Register your models here.
admin.site.register(Group)
admin.site.register(Post)
