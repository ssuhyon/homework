from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, DetailView, UpdateView
from rest_framework import generics
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer

class PostListView(ListView):
    model = Post
    template_name = 'post/post_list.html'
    context_object_name = 'posts'

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'post/post_form.html'
    fields = ['title', 'content', 'image', 'tags']
    success_url = '/api/posts/'

class PostUpdateView(UpdateView):
    model = Post
    fields = ['title', 'content', 'image', 'tags']
    template_name = 'post/post_form.html'
    success_url = '/api/posts/'

from django.shortcuts import redirect
from .models import Comment

class PostDetailView(DetailView):
    model = Post
    template_name = 'post/post_detail.html'
    context_object_name = 'post'

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        comment = Comment(
            post=self.object,
            author=request.user.username,
            text=request.POST.get('text')
        )
        comment.save()
        return redirect('api:post-detail', pk=self.object.pk)

class PostListCreateAPIView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostLikeAPIView(APIView):
    def post(self, request, pk, format=None):
        post = get_object_or_404(Post, pk=pk)
        post.likes += 1
        post.save()
        return Response({'status': 'post liked', 'likes': post.likes}, status=status.HTTP_200_OK)

class CommentListCreateAPIView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class CommentRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
