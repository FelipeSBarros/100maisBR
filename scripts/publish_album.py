from Os100maisBR.albums.models import Album
from Os100maisBR.coletaneas.models import Coletanea
from datetime import datetime, timedelta, timezone

GOOD_UNTIL = datetime.utcnow().replace(tzinfo=timezone(timedelta(hours=0))) - timedelta(
    days=2
)


def run():
    albums = Album.objects.order_by("pk").all()
    coletaneas = Coletanea.objects.filter(last_visit__gte=(GOOD_UNTIL))
    for coletanea in coletaneas:
        publicados = len(coletanea.albums.all())
        coletanea.albums.add(albums[publicados])
