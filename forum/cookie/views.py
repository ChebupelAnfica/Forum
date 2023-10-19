from django.shortcuts import render, redirect
from .models import CookieArticle
from .forms import CookieForm
from django.views.generic import DetailView, UpdateView, DeleteView


def cookie_home(request):
    cookie = CookieArticle.objects.all()
    return render(request, 'cookie/cookie_home.html', {'cookie': cookie})


class CookieDetailView(DetailView):
    model = CookieArticle
    template_name = 'cookie/details_view_cookie.html'
    context_object_name = "article"


class CookieUpdateView(UpdateView):
    model = CookieArticle
    template_name = 'cookie/create_cookie.html'
    form_class = CookieForm


class CookieDeleteView(DeleteView):
    model = CookieArticle
    template_name = 'cookie/cookie_delete.html'
    success_url = "/cookie"


def create_cookie(request):
    error = ""
    if request.method == 'POST':
        form = CookieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cookie:cookie_home')
        else:
            error = 'Ошибка: проверьте правильность заполнения формы.'
    else:
        form = CookieForm()

    context = {
        'form': form,
        'error': error,
    }

    return render(request, 'cookie/create_cookie.html', context)
