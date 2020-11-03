from db.run_sql import run_sql
from models.album import Album
from models.artist import Artist
from repositories import artist_repository

def save(album):
    sql = "INSERT INTO albums (album_title, genre, artist_id) VALUES (%s, %s, %s) RETURNING *"
    values = [album.album_title, album.genre, album.artist_id]
    results = run_sql(sql, values)
    id = results[0]['id']
    album.id = id
    return album

def select_all():
    albums = []

    sql = "SELECT * FROM albums"
    results = run_sql(sql)

    for row in results:
        artist = artist_repository.select(row['artist_id'])
        album = Album(row['album_title'], row['genre'], artist)
        albums.append(album)
    return albums
    

def select(id):
    album = None
    sql = "SELECT * FROM albums WHERE id = %s"  
    values = [id] 
    result = run_sql(sql, values)[0]
    
    if result is not None:
        artist = artist_repository.select(result['artist_id'])
        album = Album(result['album_title'], result['genre'], artist)
    return album


def albums(artist):
    albums = []

    sql = "SELECT * FROM albums WHERE artist_id = %s"
    values = [artist.id]
    results = run_sql(sql, values)

    for row in results:
        album = Album(row['album_title'], row['genre'], artist)
        albums.append(album)
    return albums

def delete_all():
    sql = "DELETE  FROM albums" 
    run_sql(sql)

def delete(id):
    sql = "DELETE  FROM albums (album_title, genre, artist_id) VALUES (%s, %s, %s) WHERE id = %s" 
    values = [id]
    run_sql(sql, values)

def update(album):
    sql = "UPDATE albums SET (album_title, genre, artist_id) VALUES (%s, %s, %s) WHERE id = %s"
    values = [album.album_title, album.genre, album.artist_id]
    run_sql(sql, values) 