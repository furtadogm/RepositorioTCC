from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy

from django.contrib.auth import get_user_model
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin, messages


class myUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = (
            "username",
            "email",
        )
        field_classes = {"username": UsernameField}


class UsuarioCreateView(CreateView):
    model = get_user_model()
    form_class = myUserCreationForm
    success_message = "Usuário cadastrado com sucesso!"
    success_url = "/"
    template_name = "registration/form.html"

    def get_context_data(self, **kwargs):
        context = super(CreateView, self).get_context_data(**kwargs)
        context["titulo"] = "Usuários - Repositório de TCC"
        context["descricao"] = "Cadastro de Usuário"
        return context

    def form_valid(self, form):
        url = super().form_valid(form)
        return url


class UsuarioUpdateView(UpdateView):
    model = get_user_model()
    fields = ["username", "first_name", "last_name"]
    success_message = "Usuário atualizado com sucesso!"
    success_url = "/"
    template_name = "registration/form.html"

    def get_object(self, queryset=None):
        return self.request.user

    def get_context_data(self, **kwargs):
        context = super(UpdateView, self).get_context_data(**kwargs)
        context["titulo"] = "Usuários - Repositório de TCC"
        context["descricao"] = "Editar Usuário"
        context["botao"] = "Salvar"
        return context

    def form_valid(self, form):
        url = super().form_valid(form)
        return url


class UsuarioDeleteView(DeleteView):
    model = get_user_model()
    success_url = reverse_lazy("index")
    template_name = "registration/excluir.html"
    success_message = "Usuário excluído com sucesso!"


class PasswordChangeView(LoginRequiredMixin, SuccessMessageMixin, PasswordChangeView):
    login_url = reverse_lazy("login")
    from_class = PasswordChangeView
    success_message = "Senha alterada com sucesso!"

    success_url = reverse_lazy("index")
