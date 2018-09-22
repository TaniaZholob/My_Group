from django.shortcuts import render
from django.utils import timezone
from .models import Post

def Main(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'Main.html', {'posts': posts})