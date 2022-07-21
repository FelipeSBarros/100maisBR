from Os100maisBR.albums.models import Album
from os import path
import csv

album_list = "100maisbr_v1.csv"
working_dir = path.abspath("./")


def run():
    with open(path.join(working_dir, album_list)) as file:
        reader = csv.reader(file)
        next(reader)  # Advance past the header

        Album.objects.all().delete()

        for row in reader:
            print(row[1])

            album = Album.objects.create(
                titulo=row[1],
                ano=row[2],
                wikipedia_link="",
                spotify_link=row[4],
                img_link=row[5],
            )
            artistas = row[3].split(",")
            for artista in artistas:
                album.artista.create(nome=artista)
