from django.urls import path
from . import views

app_name = 'client'
urlpatterns = [
    path('', views.home, name="home"),
    path('category/', views.category, name="category"),
    path('macro_and_micro/', views.macro_and_micro, name="macro_and_micro"),
    path('matchup/', views.matchup, name="matchup"),
    path('runes/', views.runes, name="runes"),
    path('items_and_builds/', views.items_and_builds, name="items_and_builds"),
    path('update_logs/', views.update_logs, name="update_logs"),
    path('blog/', views.blog, name="blog"),
    path('policy/', views.policy, name="policy"),
]
