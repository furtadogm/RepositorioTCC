from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from django.urls import reverse_lazy
from tcc.models import *


class AutorCreateView(CreateView):
    model = Autor
    fields = ["primeiro_nome", "ultimo_nome", "foto"]
    success_message = "Autor cadastrado com sucesso!"
    success_url = "/"


class AutorUpdateView(UpdateView):
    model = Autor
    fields = ["primeiro_nome", "ultimo_nome", "foto"]
    success_message = "Autor atualizado com sucesso!"
    template_name = "cadastros/form.html"
    success_url = "/"


class AutorDeleteView(DeleteView):
    model = Autor
    success_url = reverse_lazy("index")
    success_message = "Autor excluído com sucesso!"


class AutorListView(ListView):
    model = Autor
    template_name = "cadastros/listas/autores.html"
