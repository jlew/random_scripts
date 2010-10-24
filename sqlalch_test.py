from sqlalchemy import Integer, String, Column, Boolean, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from time import time
Base = declarative_base(bind=create_engine('sqlite:///tutorial.db'))
Session = sessionmaker(bind=Base.metadata.bind)


class Song(Base):
    __tablename__ = 'songs'
    song_id = Column(Integer, primary_key=True)
    title = Column(String)
    artist = Column(String)
    album = Column(String)
    played = Column(Boolean)
    time = Column(Integer)
    requester = Column(String)

    def __init__(self, id, title, artist, album, user):
        self.song_id = id
        self.title = title
        self.artist = artist
        self.album = album
        self.played = False
        self.time = time()
        self.requester = user

    def __repr__(self):
        return "<Song('%s','%s','%s')>" % \
                (self.title, self.artist, self.album)

Base.metadata.create_all()

def add_song(id, title, artist, album, user):
    session = Session()
    song_to_insert = Song(id, title, artist, album, user)
    session.add(song_to_insert)
    session.commit()
    session.close()

def get_queue():
    session = Session()
    s = session.query(Song).filter(Song.played==False).order_by(Song.time).all()
    session.close()
    return s

def next_song_play():
    session = Session()
    s = session.query(Song).filter(Song.played==False).order_by(Song.time).first()
    if s:
        s.played = True
    session.commit()
    session.close()
    return s

#add_song( 1, "test", "t2", "t3", "jlew" )
#add_song( 2, "2est", "22", "23", "2lew" )
#add_song( 3, "3est", "32", "33", "3lew" )
#add_song( 4, "4est", "42", "43", "4lew" )
#add_song( 5, "5est", "52", "53", "5lew" )


print "QUEUE",get_queue()
next_song_play()
#session = Session()
#for instance in session.query(Song).order_by(Song.song_id): 
#     print instance.song_id, instance.title, instance.time
#     instance.title = instance.title + "TEST"
#     session.add(instance)
#     session.commit()
