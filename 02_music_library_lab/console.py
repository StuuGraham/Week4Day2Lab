import pdb
from models.artist import Artist
from models.album import Album
import repositories.artist_repository as artist_repository
import repositories.album_repository as album_repository

album_repository.delete_all()
artist_repository.delete_all()

artist1 = Artist("Pendulum")
artist2 = Artist("Radiohead")
artist_repository.save(artist1)
artist_repository.save(artist2)

album1 = Album("Hold Your Colour", "Drum & Bass", artist1.id)
album2 = Album("In Rainbows", "Alternative", artist2.id)
album_repository.save(album1)
album_repository.save(album2)

artist_repository.select_all()
album_repository.select_all()

pdb.set_trace()
