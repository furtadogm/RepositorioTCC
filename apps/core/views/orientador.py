from .global_views import render, redirect, login_required

from ..forms import OrientadorForm
from ..models import Orientador

template_preffix = "orientadores"


def listar_orientadores(request):
    object_list = Orientador.objects.all()
    context = {"object_list": object_list}
    return render(request, f"{template_preffix}/listagem.html", context=context)


@login_required
def criar_orientadores(request):

    form = OrientadorForm()

    if request.method == "POST":

        form = OrientadorForm(request.POST)

        if form.is_valid():
            form.save()
            form = OrientadorForm()
            return redirect(f"listagem_{template_preffix}")

    context = {"form": form}
    return render(request, "formulario.html", context=context)


@login_required
def editar_orientadores(request, id=None):

    model = Orientador

    try:
        obj = model.objects.get(id=id)
    except model.DoesNotExist:
        return redirect(f"listagem_{template_preffix}")

    form = OrientadorForm(instance=obj)

    if request.method == "POST":

        form = OrientadorForm(request.POST, instance=obj)

        if form.is_valid():
            form.save()
            form = OrientadorForm()
            return redirect(f"listagem_{template_preffix}")

    context = {"form": form}
    return render(request, "formulario.html", context=context)


@login_required
def deletar_orientadores(request, id=None):

    model = Orientador

    try:
        obj = model.objects.get(id=id)
    except model.DoesNotExist:
        pass
    else:
        obj.delete()
    return redirect(f"listagem_{template_preffix}")
