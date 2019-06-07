from django.shortcuts import render

# Create your views here.

def blog_posts(request):
    return render(request, 'Hello')