from django.shortcuts import render
from .models import User
from .forms import *
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy


# Create your views here.


def login(request):
    return render(request, 'superuser/login.html')


def home(request):
    return render(request, 'superuser/home.html')


def blog(request):
    return render(request, 'superuser/blog.html')

def malphite_guide(request):
    return render(request, 'superuser/malphite_guide.html')

def logout(request):
    return


def validation(request):
    if request.method == "POST":
        form = UserLogin(request.POST)
    if form.is_valid():
        try:
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = User.objects.get(username=username, password=password)
            return HttpResponseRedirect(reverse_lazy('app_superuser:home'))
        except:
            messages.error(request, 'Usuario o Contraseña Incorrecta')
    else:
        form = UserLogin()
        messages.error(request, 'Usuario o Contraseña Incorrecto')
    return render(request, 'superuser/login.html', {'form': form})
