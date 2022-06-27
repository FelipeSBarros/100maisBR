from django.forms import ModelForm

from Os100maisBR.coletaneas.models import Coletanea


class ColetaneaForm(ModelForm):
    class Meta:
        model = Coletanea
