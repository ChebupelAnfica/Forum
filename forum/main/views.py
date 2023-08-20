from django.shortcuts import render

def home(request):
    return render(request, 'main/home.html')

def soft(request):
    return render(request, 'main/soft.html')

def news(request):
    return render(request, 'news/news_home.html', {'news': news})

def games(request):
    return render(request, 'main/games.html')

def cooking(request):
    return render(request, 'main/cooking.html')


def random(request):
    return render(request, 'main/random.html')



