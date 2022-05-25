from django.urls import path
from . import views

app_name = 'app_superuser'
urlpatterns = [
    path('', views.login, name="login"),
    path('home/', views.home, name="home"),
    path('validation/', views.validation, name="validation"),
    path('blog/', views.blog, name="blog"),
    path('malphite_guide/', views.malphite_guide, name="malphite_guide"),
    path('logout/', views.logout, name="logout"),
]