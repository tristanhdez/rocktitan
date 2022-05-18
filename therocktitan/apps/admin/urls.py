from django.urls import path
from . import views

app_name = 'admin_rock_titan'
urlpatterns = [
    path('', views.login, name="login"),
    path('home/', views.home, name="home"),
]
