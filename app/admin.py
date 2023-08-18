from django.contrib import admin
from .models import Post,Members,Categories,Role
# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):

    list_display = ['id', 'title', 'data']
    list_display_links = ['id', 'title']
    list_filter = ['title']

@admin.register(Members)
class MembersAdmin(admin.ModelAdmin):

    list_display = ['id', 'first_name', 'last_name', 'email']
    list_display_links = ['id', 'first_name', 'last_name']
    list_filter = ['role']
    ordering = ['first_name', 'last_name']

@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):

    list_display = ['id', 'name']
    list_display_links = ['id', 'name']

@admin.register(Categories)
class CategoryAdmin(admin.ModelAdmin):

    list_display = ['id', 'title']
    list_display_links = ['id', 'title']
