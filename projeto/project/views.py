from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from tcc.models import TCC

# @login_required
def index(request):
    queryset = TCC.objects.all()
    context = {"queryset": queryset}
    return render(request, "index.html", context)
