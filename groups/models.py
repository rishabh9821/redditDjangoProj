from django.db import models
from django.db import models
import misaka
from django.contrib.auth import get_user_model
from django import template
from django.contrib.auth.models import User
from django.urls import reverse

User = get_user_model()

register = template.Library()

class Group(models.Model):
    ## PK_URL_KWARG needs to changed to match what's shown below

    name = models.CharField(max_length=128, unique = True)
    description = models.TextField(max_length = 512)
    description_html = models.TextField(editable = False, default = '', blank = True)
    members = models.ManyToManyField(User)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('groups:group-detail', kwargs = {'group_pk': self.pk})
