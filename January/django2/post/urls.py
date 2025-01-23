from django.urls import path
from .views import PostListView, PostCreateView, PostUpdateView, PostDetailView, PostListCreateAPIView, PostRetrieveUpdateDestroyAPIView, CommentListCreateAPIView, CommentRetrieveUpdateDestroyAPIView, PostLikeAPIView

urlpatterns = [
    path('posts/', PostListView.as_view(), name='post-list'),
    path('posts/create/', PostCreateView.as_view(), name='post-create'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('posts/<int:pk>/edit/', PostUpdateView.as_view(), name='post-update'),
    path('posts/<int:pk>/like/', PostLikeAPIView.as_view(), name='post-like'),
    path('comments/', CommentListCreateAPIView.as_view(), name='comment-list-create'),
    path('comments/<int:pk>/', CommentRetrieveUpdateDestroyAPIView.as_view(), name='comment-retrieve-update-destroy'),
]