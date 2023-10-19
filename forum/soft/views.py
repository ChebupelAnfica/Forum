from django.shortcuts import render, redirect
from .models import SoftArticle
from .forms import SoftForm
from django.views.generic import DetailView, UpdateView, DeleteView

def soft_home(request):
    soft = SoftArticle.objects.all()
    return render(request, 'soft/soft_home.html', {'soft': soft})


class SoftDetailView(DetailView):
    model = SoftArticle
    template_name = 'soft/details_view_soft.html'
    context_object_name = "article"


class SoftUpdateView(UpdateView):
    model = SoftArticle
    template_name = 'soft/create_soft.html'
    form_class = SoftForm


class SoftDeleteView(DeleteView):
    model = SoftArticle
    template_name = 'soft/soft_delete.html'
    success_url = "/soft"



def create_soft(request):
    error = ""
    if request.method == 'POST':
        form = SoftForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('soft:soft_home')
        else:
            error = 'Ошибка: проверьте правильность заполнения формы.'
    else:
        form = SoftForm()

    context = {
        'form': form,
        'error': error,
    }

    return render(request, 'soft/create_soft.html', context)
