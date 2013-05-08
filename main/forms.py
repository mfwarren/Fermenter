from main.models import Brew

from django import forms

class BrewForm(forms.ModelForm):
    class Meta:
        model = Brew
        fields = ('beer_type', 'notes', 'target_temperature')
