from django.shortcuts import render, redirect
from .forms import NewsForm
from .models import NewsArticle
from django.views.generic import DetailView, UpdateView, DeleteView



def news_home(request):
    news = NewsArticle.objects.all()
    return render(request, 'news/news_home.html',  {'news': news})



class NewsDetailView(DetailView):
    model = NewsArticle
    template_name = 'news/details_view.html'
    context_object_name = "article"


class NewsUpdateView(UpdateView):
    model = NewsArticle
    template_name = 'news/create.html'
    form_class = NewsForm


class NewsDeleteView(DeleteView):
    model = NewsArticle
    template_name = 'news/news-delete.html'
    success_url = "/news"

def create(request):
    error = ""
    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news:news_home')
        else:
            error = 'Ошибка: проверьте правильность заполнения формы.'
    else:
        form = NewsForm()

    context = {
        'form': form,
        'error': error,
    }

    return render(request, 'news/create.html', context)
