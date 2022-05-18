from django.shortcuts import render
from .models import *


# Create your views here.


def home(request):
    return render(request,"client/home.html")


def category(request):
    return render(request,"client/category.html")


def macro_and_micro(request):
    return render(request,"client/macro_and_micro.html")


def policy(request):
    return render(request,"client/policy.html")


def matchup(request):
    matchup = Matchup.objects.all()
    #messages.success(request,'Courses listed!')
    return render(request,"client/matchup.html", {"matchup":matchup})


def runes(request):
    return render(request,"client/runes.html")


def items_and_builds(request):
    return render(request,"client/items_and_builds.html")


def update_logs(request):
    update_logs = Update.objects.all()
    return render(request,"client/update_logs.html", {"update_logs":update_logs})


def blog(request):
    return render(request,"client/blog.html")