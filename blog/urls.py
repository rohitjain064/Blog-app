from django.urls import path
from.views import *

urlpatterns=[
    path('',PostListView.as_view(),name='blog-home'),
    path('post/<int:pk>',PostDetailListView.as_view(),name='post-detail'),
    path('post/new/',PostCreateView.as_view(),name='post-create'),
    path('post/<int:pk>/update/',PostUpdateView.as_view(),name='post-update'),
    path('post/<int:pk>/delete/',PostDeletetView.as_view(),name='post-delete'),
    path('user/<str:username>',UserPostListView.as_view(),name='user-posts'),
    path('about/',about,name='blog-about'),

]