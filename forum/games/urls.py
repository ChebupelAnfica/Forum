from django.urls import path
from . import views

app_name = 'games'

urlpatterns = [
    path('', views.games_home, name='games_home'),
    path('create_games', views.create_games, name='create_games'),
    path('<int:pk>', views.GameDetailView.as_view(), name='game-detail'),
    path('<int:pk>/update', views.GamesUpdateView.as_view(), name='games-update'),
    path('<int:pk>/delete', views.GamesDeleteView.as_view(), name='games-delete'),
]