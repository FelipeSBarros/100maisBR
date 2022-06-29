from django.urls import path

from Os100maisBR.coletaneas.views import create_coletanea, detalhe_coletanea

app_name = "coletaneas"

urlpatterns = [
    path("nova/", create_coletanea, name="new"),
    path("<str:slug>", detalhe_coletanea, name="detail"),
]
