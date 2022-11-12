from .global_views import render, redirect, login_required

from ..forms import AutorForm
from ..models import Autor


template_preffix = "autores"


def listar_autores(request):
    object_list = Autor.objects.all()
    context = {"object_list": object_list}
    return render(request, f"{template_preffix}/listagem.html", context=context)


@login_required
def criar_autores(request):

    form = AutorForm()

    if request.method == "POST":

        form = AutorForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect(f"listagem_{template_preffix}")

    context = {"form": form}
    return render(request, "formulario.html", context=context)


@login_required
def editar_autores(request, id=None):

    model = Autor

    try:
        obj = model.objects.get(id=id)
    except model.DoesNotExist:
        return redirect(f"listagem_{template_preffix}")

    form = AutorForm(instance=obj)

    if request.method == "POST":

        form = AutorForm(request.POST, instance=obj)

        if form.is_valid():
            form.save()
            form = AutorForm()
            return redirect(f"listagem_{template_preffix}")

    context = {"form": form}
    return render(request, "formulario.html", context=context)


@login_required
def deletar_autores(request, id=None):

    model = Autor

    try:
        obj = model.objects.get(id=id)
    except model.DoesNotExist:
        pass
    else:
        obj.delete()
    return redirect(f"listagem_{template_preffix}")
