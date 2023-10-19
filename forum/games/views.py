from django.shortcuts import render, redirect
from .models import GamesArticle
from .forms import GameForm
from django.views.generic import DetailView, UpdateView, DeleteView

def games_home(request):
    games = GamesArticle.objects.all()
    return render(request, 'games/games_home.html', {'games': games})


class GameDetailView(DetailView):
    model = GamesArticle
    template_name = 'games/details_view_games.html'
    context_object_name = "article"

class GamesUpdateView(UpdateView):
    model = GamesArticle
    template_name = 'games/create_games.html'
    form_class = GameForm


class GamesDeleteView(DeleteView):
    model = GamesArticle
    template_name = 'games/games-delete.html'
    success_url = "/games"




def create_games(request):
    error = ""
    if request.method == 'POST':
        form = GameForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('games:games_home')
        else:
            error = 'Ошибка: проверьте правильность заполнения формы.'
    else:
        form = GameForm()

    context = {
        'form': form,
        'error': error,
    }

    return render(request, 'games/create_games.html', context)