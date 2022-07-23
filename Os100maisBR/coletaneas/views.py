from django.views.generic import CreateView, DetailView

from Os100maisBR.coletaneas.Mixins import EmailCreateView
from Os100maisBR.coletaneas.forms import ColetaneaForm
from Os100maisBR.coletaneas.models import Coletanea

create_coletanea = CreateView.as_view(model=Coletanea, form_class=ColetaneaForm)
# create_coletanea = EmailCreateView.as_view(
#     model=Coletanea,
#     form_class=ColetaneaForm,
#     email_subject='Confirmação de criação nova coletânea')


detalhe_coletanea = DetailView.as_view(model=Coletanea, slug_field="slug")
