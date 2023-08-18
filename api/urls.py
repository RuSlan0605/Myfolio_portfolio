from django.urls import path
from rest_framework import routers
from .views import PostViewSet, CategoryViewSet, MembersViewSet, RoleViewSet

router = routers.DefaultRouter()

router.register('member', MembersViewSet, basename='members')
router.register('post', PostViewSet, basename='posts')
router.register('category', CategoryViewSet, basename='categories')
router.register('role', RoleViewSet, 'roles')

urlpatterns = [

] + router.urls
