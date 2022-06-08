from django.contrib import admin
from Os100maisBR.albums.models import Album, Artista


class AlbumModelAdmin(admin.ModelAdmin):
    list_display = (
        "titulo",
        "ano",
    )
    date_hierarchy = "created_at"
    search_fields = (
        "titulo",
        "ano",
    )


class ArtistaModelAdmin(admin.ModelAdmin):
    list_display = ("nome",)
    date_hierarchy = "created_at"
    search_fields = ("nome",)


admin.site.register(Album, AlbumModelAdmin)
admin.site.register(Artista, ArtistaModelAdmin)
