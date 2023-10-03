from django.shortcuts import render
from django.utils import timezone 
from .models import Post

def post_list(request):
    posts = Post.objects.filter(created_date=timezone.now()).order_by('created_date')
    return render(request, 'post_list.html', {'posts': posts})