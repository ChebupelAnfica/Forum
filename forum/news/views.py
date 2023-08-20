from django.shortcuts import render, redirect
from .forms import NewsForm
from .models import NewsArticle

def news(request):
    news = NewsArticle.objects.all()
    return render(request, 'news/news_home.html', {'news': news})

def create_news(request):
    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news:list')
    else:
        form = NewsForm()

    context = {'form': form}
    return render(request, 'news/create.html', context)