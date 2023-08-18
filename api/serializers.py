from rest_framework import serializers
from app.models import Post
from app.models import Members
from app.models import Role
from app.models import Categories

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

class MembersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Members
        fields = '__all__'

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = '__all__'

