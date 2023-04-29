import datetime

import peewee
import sqlite3

db = peewee.SqliteDatabase('my_music.db')


class BaseTable(peewee.Model):
    class Meta:
        database = db


class Artist(BaseTable):
    name = peewee.CharField()


class Album(BaseTable):
    artist = peewee.ForeignKeyField(Artist)
    title = peewee.CharField()
    release_date = peewee.DateTimeField()
    publisher = peewee.CharField()
    media_type = peewee.CharField()


# db.create_tables([Artist, Album])
#
# new_art = Artist(name='Glukoza')
# new_art.save()
#
# new_album = Album.create(artist=new_art,
#                          title='Nevesta',
#                          release_date=datetime.date(day=1, month=1, year=2001),
#                          publisher='1Channal',
#                          media_type='TV',
#                          )
#
#
# bands = ["MXPX", "Kutless", "Thousand Foot Krutch"]
#
# for band in bands:
#     Artist.create(name=band)
#
#
# albums = [
#     {
#         "artist": new_art,
#         "title": "Hell is for Wimps",
#         "release_date": datetime.date(1990, 7, 31),
#         "publisher": "Sparrow",
#         "media_type": "CD"
#     },
#     {
#         "artist": new_art,
#         "title": "Love Liberty Disco",
#         "release_date": datetime.date(1999, 11, 16),
#         "publisher": "Sparrow",
#         "media_type": "CD"
#     },
#     {
#         "artist": new_art,
#         "title": "Thrive",
#         "release_date": datetime.date(2002, 3, 26),
#         "publisher": "Sparrow",
#         "media_type": "CD"
#     }
# ]
#
# for album_data in albums:
#     alb = Album.create(**album_data)
Album.delete().where(Album.id > 2).execute()

for album in Album.select().join(Artist):
    print(album.title)
    # album.title += '!'
    # album.save()


# print(Album.get(Album.id == 1).all)
