from itertools import count
from typing import List
from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from groups.models import Group
from django.urls import reverse, reverse_lazy
from django.contrib.auth import get_user_model
# Create your views here.


## Create Group #

class CreateGroupView(LoginRequiredMixin, CreateView):

    ## Login Required Fields
    login_url = 'accounts/login/'
    redirect_field_name = '/'

    ## Create View Required Fields
    model = Group
    template_name = "groups/createGroup.html"
    pk_url_kwarg = 'group_pk'
    context_object_name = 'group_form'
    fields = ('name', 'description')

    def form_valid(self, form):
        user = get_user_model()
        group = form.save(commit = False)
        group.member = user
        group.save()
        return super().form_valid(form)


## List all groups

class GroupListView(ListView):
    model = Group
    template_name = 'groups/groupList.html'
    pk_url_kwarg = 'group_pk'
    context_object_name = 'groups'

    # def get_queryset(self):
    #     return Group.objects.all().values('members').annotate(memberCount=count('members')).order_by('-memberCount')


## Group Detail View

class GroupDetailView(DetailView):
    model = Group
    template_name = 'groups/groupDetail.html'
    pk_url_kwarg = 'group_pk'
    context_object_name = 'group'


## List my groups

class MyGroupListView(ListView, LoginRequiredMixin):
    ## Login Required Fields
    login_url = 'accounts/login/'
    redirect_field_name = '/'

    ## List View Fields
    model = Group
    template_name = 'groups/myGroupList.html'
    pk_url_kwarg = 'group_pk'
    context_object_name = 'groups'

    ## Queryset
    def get_queryset(self):
        return Group.objects.filter(members__exact = self.request.user)

## Delete Group

class DeleteGroupView(LoginRequiredMixin, DeleteView):
    ## Login Required Fields
    login_url = 'accounts/login/'
    redirect_field_name = '/'

    ## Delete View Fields
    model = Group
    template_name = 'groups/deleteGroup.html'
    pk_url_kwarg = 'group_pk'
    context_object_name = 'form'
    success_url = reverse_lazy('/')
