''' Views '''

from rest_framework.generics import ListAPIView, RetrieveAPIView
from blogs.models import User, Blog_Post
from .serializers import UserSerializer, Blog_PostSerializer

class UserView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class BlogPostView(ListAPIView):
    queryset = Blog_Post.objects.all()
    serializer_class = Blog_PostSerializer

