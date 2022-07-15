from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'groups'

urlpatterns = [
    path('createGroup/', views.CreateGroupView.as_view(), name='group-create'), 
    path('', views.GroupListView.as_view(), name='group-list'),
    path('myGroups', views.MyGroupListView.as_view(), name='group-list-my'),
    path('deleteGroup/<group_pk>/', views.DeleteGroupView.as_view(), name='group-delete'),
    path('<group_pk>/', views.GroupDetailView.as_view(), name='group-detail'),
]