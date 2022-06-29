from django.views.generic import CreateView, DetailView

from Os100maisBR.coletaneas.forms import ColetaneaForm
from Os100maisBR.coletaneas.models import Coletanea

create_coletanea = CreateView.as_view(model=Coletanea, form_class=ColetaneaForm)

detalhe_coletanea = DetailView.as_view(model=Coletanea, slug_field="slug")
