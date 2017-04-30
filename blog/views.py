from django.shortcuts import render
from django.http import HttpResponse
from .models import Post


def index(request):
    post_list = Post.objects.all()
    return render(request,'blog/index.html',context={'post_list':post_list})

# Create your views here.
def detal(request,pk):
    post = get_obiect_or_404(Post,pk=pk)
    return render(request,'blog/detail.html',context={'post':post})
