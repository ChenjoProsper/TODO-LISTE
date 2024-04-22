from django import forms
from .models import Tache

class AjouteTache(forms.ModelForm):
    class Meta:
        model = Tache
        fields = ('nom','finish','description')