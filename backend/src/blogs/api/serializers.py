from rest_framework import serializers

from blogs.models import User, Blog_Post

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password')

class Blog_PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog_Post
        fields = ('id', 'pub_date', 'user', 'content')