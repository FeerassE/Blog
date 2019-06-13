from blogs.api.views import UserViewSet, Blog_PostViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'posts', Blog_PostViewSet, basename='blog-posts')
router.register(r'', UserViewSet, basename='users')
urlpatterns = router.urls









# from django.urls import path

# from .views import UserView, BlogPostView

# urlpatterns = [
#     path('', BlogPostView.as_view())
# ]