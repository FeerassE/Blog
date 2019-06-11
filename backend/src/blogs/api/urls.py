from django.urls import path

from .views import UserView, BlogPostView

urlpatterns = [
    path('', BlogPostView.as_view())
]