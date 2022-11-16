from .global_views import render, redirect, login_required

from ..forms import TCCForm
from ..models import TCC

template_preffix = "tccs"


def listar_tccs(request):
    object_list = TCC.objects.all()
    context = {"object_list": object_list}
    return render(request, f"{template_preffix}/listagem.html", context=context)


@login_required
def criar_tccs(request):

    form = TCCForm()

    if request.method == "POST":

        form = TCCForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            form = TCCForm()
            return redirect(f"listagem_{template_preffix}")

    context = {"form": form}
    return render(request, "formulario.html", context=context)


@login_required
def editar_tccs(request, id=None):

    model = TCC

    try:
        obj = model.objects.get(id=id)
    except model.DoesNotExist:
        return redirect(f"listagem_{template_preffix}")

    form = TCCForm(instance=obj)

    if request.method == "POST":

        form = TCCForm(request.POST, instance=obj)

        if form.is_valid():
            form.save()
            form = TCCForm()
            return redirect(f"listagem_{template_preffix}")

    context = {"form": form}
    return render(request, "formulario.html", context=context)


@login_required
def deletar_tccs(request, id=None):

    model = TCC

    try:
        obj = model.objects.get(id=id)
    except model.DoesNotExist:
        pass
    else:
        obj.delete()
    return redirect(f"listagem_{template_preffix}")
