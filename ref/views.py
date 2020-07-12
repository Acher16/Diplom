from django.shortcuts import render
from .models import Ref
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User

def home(request):
    return render(request, 'ref/home.html', {'title': 'Главная страница'})


class RefCreate(LoginRequiredMixin, CreateView):
    model = Ref
    fields = ['title', 'site_url', 'slug']

    def get_context_data(self, *, object_list=None, **kwargs):
        ctx = super(RefCreate, self).get_context_data(**kwargs)
        ctx['title'] = 'Создание ссылок'
        ctx['refs'] = Ref.objects.all().order_by('-number')
        return ctx


    def form_valid(self, form):
        form.instance.avtor = self.request.user
        return super().form_valid(form)





