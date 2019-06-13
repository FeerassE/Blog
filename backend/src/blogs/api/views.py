''' Views '''

from rest_framework import viewsets
from blogs.models import User, Blog_Post
from .serializers import UserSerializer, Blog_PostSerializer


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

class Blog_PostViewSet(viewsets.ModelViewSet):
    serializer_class = Blog_PostSerializer
    queryset = Blog_Post.objects.all()



# from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
# from blogs.models import User, Blog_Post
# from .serializers import UserSerializer, Blog_PostSerializer


# class UserView(RetrieveAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

    
# class BlogPostView(ListAPIView):
#     queryset = Blog_Post.objects.all()
#     serializer_class = Blog_PostSerializer

