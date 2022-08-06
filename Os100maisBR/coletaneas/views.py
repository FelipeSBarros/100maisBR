from django.views.generic import CreateView, DetailView
from Os100maisBR.coletaneas.Mixins import EmailCreateView
from django.contrib import messages
from Os100maisBR.coletaneas.forms import ColetaneaForm
from Os100maisBR.coletaneas.models import Coletanea
from datetime import datetime, timedelta, timezone

GOOD_UNTIL = datetime.utcnow().replace(tzinfo=timezone(timedelta(hours=0))) - timedelta(
    days=2
)

create_coletanea = CreateView.as_view(model=Coletanea, form_class=ColetaneaForm)


class ColetaneaDetailView(DetailView):
    model = Coletanea
    slug_field = "slug"

    def get_object(self):
        object = super().get_object()
        object.last_visit = datetime.now()
        object.save()
        return object


detalhe_coletanea = ColetaneaDetailView.as_view()
