from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.home, name='home'),
    path('soft/', views.soft, name='soft'),
    path('news/', views.news, name='news'),
    path('games/', views.games, name='games'),
    path('cooking/', views.cooking, name='cooking'),
    path('random/', views.cooking, name='random'),
]