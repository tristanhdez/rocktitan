from django.urls import path
from . import views


urlpatterns = [
    path('', views.home),
    path('category/', views.category),
    path('macro_and_micro/', views.macro_and_micro),
    path('matchup/', views.matchup),
    path('runes/', views.runes),
    path('items_and_builds/', views.items_and_builds),
    path('update_logs/', views.update_logs),
    path('blog/', views.blog),
]
