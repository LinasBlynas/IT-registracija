from .models import Komentarai, DarbuSarasas, Naujienos
from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm, DateInput
from tinymce.widgets import TinyMCE


class KomentaroForm(forms.ModelForm):
    turinys = forms.CharField(
        widget=forms.Textarea(attrs={'style': 'height: 80px; width: 400px;'}),
    )

    class Meta:
        model = Komentarai
        fields = ('turinys', 'darbas', 'komentatorius',)
        widgets = {'darbas': forms.HiddenInput(), 'komentatorius': forms.HiddenInput()}


class DarbuSarasasForm(forms.ModelForm):
    pastaba = forms.CharField(
        widget=forms.Textarea(attrs={'style': 'height: 80px; width: 400px;'}),
    )

    class Meta:
        model = DarbuSarasas
        fields = ('darbuotojas', 'darbai', 'laikas', 'pastaba',)
        widgets = {
            'klientai': forms.HiddenInput(),
            'padaryta': forms.HiddenInput(),
            'laikas': forms.DateInput(
                format='%Y-%m-%d',
                attrs={
                    'type': 'date',
                    'autocomplete': 'off',
                    'placeholder': 'Pasirinkite datą',
                }

            ),
        }


class NaujienosForm(forms.ModelForm):
    naujiena = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))

    class Meta:
        model = Naujienos
        fields = ['antraste', 'naujiena']