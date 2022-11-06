from django import forms
from .models import Curso, TCC


class TCCForm(forms.ModelForm):
    model = TCC
    fields = "__all__"
    exclude = ("usuario",)
