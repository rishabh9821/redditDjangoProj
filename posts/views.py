from itertools import count
from typing import List
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from groups.models import Group
from django.urls import reverse, reverse_lazy
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from posts.forms import PostForm
from posts.models import Post
from django.http import HttpResponseRedirect
# Create your views here.

## Create Post View #
# Group Primary Key needs to be passed into function

@login_required
def CreatePostView(request, group_pk):
    group = get_object_or_404(Group, pk = group_pk)

    if request.method == 'POST':

        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit = False)
            post.user = request.user
            post.group = group
            post.save()
            return HttpResponseRedirect(reverse('posts:post-detail', kwargs={'post_pk': post.pk}))
    else:
        form = PostForm()

    return render(request, "posts/createPost.html", context = {"form":form})



# @login_required
# def CreatePostView(request, group_pk):
#     group = get_object_or_404(Group, pk = group_pk)
#     user = get_user_model()

#     if request.method == 'POST':

#         form = PostForm(request.POST)
#         if form.is_valid():
#             post = form.save(commit = False)
#             post.group = group
#             post.user = user
#             post.save()
#             return HttpResponseRedirect(reverse('posts:post-detail', kwargs={'post_pk': post.pk}))
#     else:
#         form = PostForm()

#     return render(request, "posts/createPost.html", context = {"form":form})

## List View of all Posts
# Need all posts for each specific group
# Group_pk needs to passed into function


#### MAY NOT BE NECESSARY SINCE THIS IS ACHIEVED IN (groups:group-detail)
# def PostListView(request, group_pk):
#     groupPicked = get_object_or_404(Group, pk = group_pk)
#     posts = Post.objects.filter(group__exact = groupPicked).order_by('-createTime')
#     return render(request, 'posts/postList.html', context = {'posts': posts})


## List View of all User Posts
class MyPostListView(ListView, LoginRequiredMixin):

    ## Login Required Fields
    login_url = 'accounts/login/'
    redirect_field_name = '/'

    ## Create View Required Fields
    model = Post
    template_name = "posts/myPostList.html"
    pk_url_kwarg = 'post_pk'
    context_object_name = 'posts'

    # Need to get posts from a specific user
    def get_queryset(self):
        user = self.request.user
        return Post.objects.filter(user__exact = user).order_by('-createTime')

### NEED POST DETAIL VIEW BELOW

class PostDetailView(DetailView):
    model = Post
    context_object_name = 'post'
    template_name = 'posts/postDetail.html'
    pk_url_kwarg = 'post_pk'