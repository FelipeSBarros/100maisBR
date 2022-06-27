from django.shortcuts import render
from django.views.generic import CreateView
from Os100maisBR.coletaneas.models import Coletanea


class CreateColetanea(CreateView):
    model = Coletanea
    fields = ["nome_coletanea", "email"]
