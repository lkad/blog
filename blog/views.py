from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request,'blog/index.html',context={'title':'my index bolg','welcom':'welcom to my blog'})

# Create your views here.
