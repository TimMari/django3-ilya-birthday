from django.shortcuts import render
from .models import MainImg, Info, VidSport, VidGame, VidOther, BlogModel


def index(request):
    info = Info.objects.order_by('-id')[:3]
    img = MainImg.objects.order_by('-id')[:1]
    return render(request, 'mainn/index.html', {'img': img, 'info': info})


def video(request):
    game = VidGame.objects.order_by('-id')
    vid = VidSport.objects.order_by('-id')
    other = VidOther.objects.order_by('-id')
    return render(request, 'mainn/vidos.html', {'game':game, 'vid':vid, 'other':other})


def blog(request):
    blogM = BlogModel.objects.order_by('-id')
    return render(request, 'mainn/blog.html', {'blog': blogM})



