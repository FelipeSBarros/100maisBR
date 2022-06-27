from django.contrib import admin
from Os100maisBR.coletaneas.models import Coletanea


class ColetaneaModelAdmin(admin.ModelAdmin):
    list_display = (
        "nome_coletanea",
        "slug",
        "email",
    )
    date_hierarchy = "created_at"
    search_fields = (
        "nome_coletanea",
        "email",
    )


admin.site.register(Coletanea, ColetaneaModelAdmin)
