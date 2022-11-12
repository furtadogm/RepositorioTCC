from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.index, name="index"),
    # autores
    #
    path("autores/", views.listar_autores, name="listagem_autores"),
    path("autores/criar/", views.criar_autores, name="criar_autores"),
    path("autores/<int:id>/editar/", views.editar_autores, name="editar_autores"),
    path("autores/<int:id>/deletar/", views.deletar_autores, name="deletar_autores"),
    # path("autores/tccs/", views.listar_tccs_pelo_autor, name="listar_tcc_autor"),
    # orientadores
    #
    path("orientadores/", views.listar_orientadores, name="listagem_orientadores"),
    path("orientadores/criar/", views.criar_orientadores, name="criar_orientadores"),
    path(
        "orientadores/<int:id>/editar/",
        views.editar_orientadores,
        name="editar_orientadores",
    ),
    path(
        "orientadores/<int:id>/deletar/",
        views.deletar_orientadores,
        name="deletar_orientadores",
    ),
    # cursos
    #
    path("cursos/", views.listar_cursos, name="listagem_cursos"),
    path("cursos/criar/", views.criar_cursos, name="criar_cursos"),
    path("cursos/<int:id>/editar/", views.editar_cursos, name="editar_cursos"),
    path("cursos/<int:id>/deletar/", views.deletar_cursos, name="deletar_cursos"),
    # tccs
    #
    path("tccs/", views.listar_tccs, name="listagem_tccs"),
    path("tccs/criar/", views.criar_tccs, name="criar_tccs"),
    path("tccs/<int:id>/editar/", views.editar_tccs, name="editar_tccs"),
    path("tccs/<int:id>/deletar/", views.deletar_tccs, name="deletar_tccs"),
    # usuario
    #
    path("registration/", views.UsuarioCreateView.as_view(), name="registration"),
    path("update/<int:pk>/", views.UsuarioUpdateView.as_view(), name="update"),
    path("delete/<int:pk>/", views.UsuarioDeleteView.as_view(), name="delete"),
    path(
        "password/",
        views.PasswordChangeView.as_view(template_name="cadastros/mudar-senha.html"),
        name="password",
    ),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
