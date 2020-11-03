from db.run_sql import run_sql
from models.artist import Artist
from models.album import Album
from repositories import album_repository

def save(artist):
    sql = "INSERT INTO artists (name) VALUES (%s) RETURNING *"
    values = [artist.name]
    results = run_sql(sql, values)
    id = results[0]['id']
    artist.id = id
    return artist

def select_all():  
    artists = [] 

    sql = "SELECT * FROM artists"
    results = run_sql(sql)

    for row in results:
        artist = Artist(row['name'], row['id'])
        artists.append(artist)
    return artists 
    

def select(id):
    artist = None
    sql = "SELECT * FROM artists WHERE id = %s"  
    values = [id] 
    result = run_sql(sql, values)[0]
    
    if result is not None:
        artist = Artist(result['name'], result['id'] )
    return artist

def artists(album):
    artists = []

    sql = "SELECT * FROM artists WHERE album_id = %s"
    values = [album.id]
    results = run_sql(sql, values)

    for row in results:
        artist = Artist(row['name'], album)
        artists.append(artist)
    return artists

def delete_all():
    sql = "DELETE FROM artists" 
    run_sql(sql)

def delete(id):
    sql = "DELETE  FROM artists (name) VALUES (%s) WHERE id = %s" 
    values = [id]
    run_sql(sql, values)


def update(artist):
    sql = "UPDATE artists SET (name) VALUES (%s) WHERE id = %s"
    values = [artist.name]
    run_sql(sql, values)