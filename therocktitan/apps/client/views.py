from django.shortcuts import render
from .models import *


# Create your views here.


def home(request):
    return render(request,"home.html")


def category(request):
    return render(request,"category.html")


def macro_and_micro(request):
    return render(request,"macro_and_micro.html")


def matchup(request):
    matchup = Matchup.objects.all()
    #messages.success(request,'Courses listed!')
    return render(request,"matchup.html", {"matchup":matchup})


def runes(request):
    return render(request,"runes.html")


def items_and_builds(request):
    return render(request,"items_and_builds.html")


def update_logs(request):
    return render(request,"items_and_builds.html")


def blog(request):
    return render(request,"blog.html")