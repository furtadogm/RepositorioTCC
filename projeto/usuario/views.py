from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import UserCreationForm, UsernameField
from usuario.models import Usuario
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
    # fields = ["username", "email", "password1", "password2"]
    form_class = myUserCreationForm
    success_message = "Usuário cadastrado com sucesso!"
    success_url = "/"


class UsuarioUpdateView(UpdateView):
    model = get_user_model()
    fields = ["username", "first_name", "last_name"]
    success_message = "Usuário atualizado com sucesso!"
    template_name = "usuario/usuario_form.html"
    success_url = "/"


class UsuarioDeleteView(DeleteView):
    model = get_user_model()
    success_url = reverse_lazy("index")
    success_message = "Usuário excluído com sucesso!"


# class UsuarioDetailView(LoginRequiredMixin, DetailView):
#     login_url = reverse_lazy("login")
#     model = get_user_model()
#     template_name = "usuario/usuario_detail.html"

#     def get_object(self, queryset=None):
#         return self.request.user


class PasswordChangeView(LoginRequiredMixin, SuccessMessageMixin, PasswordChangeView):
    login_url = reverse_lazy("login")
    from_class = PasswordChangeView
    success_message = "Senha alterada com sucesso!"

    success_url = reverse_lazy("index")
