from django.urls import path
from Os100maisBR.coletaneas.views import CreateColetanea

app_name = "coletaneas"

urlpatterns = [
    path("new/", CreateColetanea.as_view(), name="new"),
    # path("<slug:slug>", ArticleDetailView.as_view(), name="article_detail"),
]
