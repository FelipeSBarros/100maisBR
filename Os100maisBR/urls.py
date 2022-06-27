from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("Os100maisBR.core.urls")),
    path("coletaneas/", include("Os100maisBR.coletaneas.urls")),
]
