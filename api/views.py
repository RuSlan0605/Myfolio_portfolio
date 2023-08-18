from django.shortcuts import render
from .serializers import PostSerializer, MembersSerializer, RoleSerializer, CategorySerializer
from app.models import Post, Members, Role, Categories
from rest_framework import generics
from rest_framework import viewsets


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class MembersViewSet(viewsets.ModelViewSet):
    queryset = Members.objects.all()
    serializer_class = MembersSerializer

class RoleViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Categories.objects.all()
    serializer_class = CategorySerializer
    