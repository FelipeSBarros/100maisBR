from django.contrib import admin
from django.urls import path
from Os100maisBR.core.views import home
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home')
]
