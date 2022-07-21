from Os100maisBR.albums.models import Album
from Os100maisBR.coletaneas.models import Coletanea


def run():
    albums = Album.objects.order_by('pk').all()
    coletaneas = Coletanea.objects.all()
    for coletanea in coletaneas:
        publicados = len(coletanea.albums.all())
        coletanea.albums.add(albums[publicados])
