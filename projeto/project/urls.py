from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from usuario.views import *
from tcc.views import *
from django.conf import settings
from django.conf.urls.static import static

from .views import index

urlpatterns = [
    path("", index, name="index"),
    path("admin/", admin.site.urls),
    path("login/", auth_views.LoginView.as_view(), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("registration/", UsuarioCreateView.as_view(), name="registration"),
    path("update/<int:pk>/", UsuarioUpdateView.as_view(), name="update"),
    path("delete/<int:pk>/", UsuarioDeleteView.as_view(), name="delete"),
    path(
        "password/",
        PasswordChangeView.as_view(template_name="cadastros/mudar-senha.html"),
        name="password",
    ),
    # path("criar/autor/", AutorCreateView.as_view(), name="criar_autor"),
    # path("editar/autor/<int:pk>/", AutorUpdateView.as_view(), name="editar_autor"),
    # path("deletar/autor/<int:pk>/", AutorDeleteView.as_view(), name="deletar_autor"),
    # path("listar/autores/", AutorListView.as_view(), name="listar_autores"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
