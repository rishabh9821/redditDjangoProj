from django.contrib import admin
from django.urls import path, include
from posts import views

#

app_name = 'posts'

urlpatterns = [
    path('group/<group_pk>/createPost/', views.CreatePostView, name='post-create'),
    path('myPosts/', views.MyPostListView.as_view(), name = 'post-list-my'),
    path('<post_pk>', views.PostDetailView.as_view(), name = 'post-detail'),

]