from re import A
from django.shortcuts import render
from rest_framework import generics
from blog.models import Post
from blog.serializers import PostSerializer



 
class PostList(generics.ListCreateAPIView):
    queryset = Post.postobjects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
