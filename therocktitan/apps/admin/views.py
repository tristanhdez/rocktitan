from django.shortcuts import render
from ..client.models import *
from .forms import *
from django.contrib import messages


# Create your views here.

def login(request):
    return render(request, "admin/login.html")


def home(request):
    if request.method == "POST":
        form = UserLogin(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            try:
                if username == "titan" and  password == "123":
                    return render(request, 'admin/home.html', {'username': username})
            except:
                messages.error(request, 'Usuario o Contraseña Incorrecta')