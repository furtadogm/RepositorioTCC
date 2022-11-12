from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


SAFE_METHODS = ["GET", "OPTIONS"]


def index(request):
    usuario_logado = request.user.is_authenticated
    context = {"usuario_logado": usuario_logado}
    return render(request, "index.html", context=context)
