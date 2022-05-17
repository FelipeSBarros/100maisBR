from django.urls import path
from Os100maisBR.core.views import HomeView

app_name = "core"

urlpatterns = [
    path("", HomeView, name="home"),
]
