from django import forms

from django.contrib.admin.widgets import AdminDateWidget

from .models import *


class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        # fields = "__all__"
        exclude = ["foto_thumbnail"]


class OrientadorForm(forms.ModelForm):
    class Meta:
        model = Orientador
        fields = "__all__"


class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = "__all__"


class TCCForm(forms.ModelForm):

    # ano_de_publicacao = forms.DateField(widget=AdminDateWidget())

    class Meta:
        model = TCC
        fields = "__all__"
        widgets = {"ano_de_publicacao": forms.widgets.DateInput(attrs={"type": "date"})}
