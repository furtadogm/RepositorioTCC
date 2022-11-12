from .global_views import render, redirect, login_required

from ..forms import CursoForm
from ..models import Curso

template_preffix = "cursos"


def listar_cursos(request):
    object_list = Curso.objects.all()
    context = {"object_list": object_list}
    return render(request, f"{template_preffix}/listagem.html", context=context)


@login_required
def criar_cursos(request):

    form = CursoForm()

    if request.method == "POST":

        form = CursoForm(request.POST)

        if form.is_valid():
            form.save()
            form = CursoForm()
            return redirect(f"listagem_{template_preffix}")

    context = {"form": form}
    return render(request, "formulario.html", context=context)


@login_required
def editar_cursos(request, id=None):

    model = Curso

    try:
        obj = model.objects.get(id=id)
    except model.DoesNotExist:
        return redirect(f"listagem_{template_preffix}")

    form = CursoForm(instance=obj)

    if request.method == "POST":

        form = CursoForm(request.POST, instance=obj)

        if form.is_valid():
            form.save()
            form = CursoForm()
            return redirect(f"listagem_{template_preffix}")

    context = {"form": form}
    return render(request, "formulario.html", context=context)


@login_required
def deletar_cursos(request, id=None):

    model = Curso

    try:
        obj = model.objects.get(id=id)
    except model.DoesNotExist:
        pass
    else:
        obj.delete()
    return redirect(f"listagem_{template_preffix}")
