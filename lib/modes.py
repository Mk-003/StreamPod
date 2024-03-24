from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
from sqlalchemy import ForeignKey, Table, Column, Integer, String, DateTime
from sqlalchemy.orm import relationship, backref
from sqlalchemy.orm import declarative_base



Base = declarative_base()


movie_viewer = Table(
    'movie_viewers',
    Base.metadata,
    Column('movie_id', ForeignKey('movies.id'), primary_key=True),
    Column('viewer_id', ForeignKey('viewers.id'), primary_key=True),
    extend_existing=True,
)

class Movie(Base):
    __tablename__ = 'movies'

    id = Column(Integer(), primary_key=True)
    title = Column(String())
    genre = Column(String())
    platform = Column(String())
    price = Column(Integer())
    created_at = Column(DateTime(), server_default=func.now())
    updated_at = Column(DateTime(), onupdate=func.now())

    viewers = relationship('Viewer', secondary=movie_viewer, back_populates='movies')
    comments = relationship('Comment', backref=backref('movie'))

    def __repr__(self):
        return f'Movie(id={self.id}, ' + \
            f'title={self.title}, ' + \
            f'platform={self.platform})'

class Viewer(Base):
    __tablename__ = 'viewers'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    created_at = Column(DateTime(), server_default=func.now())
    updated_at = Column(DateTime(), onupdate=func.now())

    movies = relationship('Movie', secondary=movie_viewer, back_populates='viewers')
    comments = relationship('Comment', backref=backref('viewer'))

    def __repr__(self):
        return f'Viewer(id={self.id}, ' + \
            f'name={self.name})'

class Comment(Base):
    __tablename__ = 'comments'

    id = Column(Integer(), primary_key=True)

    score = Column(Integer())
    content = Column(String())
    created_at = Column(DateTime(), server_default=func.now())
    updated_at = Column(DateTime(), onupdate=func.now())

    movie_id = Column(Integer(), ForeignKey('movies.id'))
    viewer_id = Column(Integer(), ForeignKey('viewers.id'))

    def __repr__(self):
        return f'Comment(id={self.id}, ' + \
            f'score={self.score}, ' + \
            f'movie_id={self.movie_id})'



if __name__=='__main__':
   engine = create_engine('sqlite:///pod.db')
   Base.metadata.create_all(engine)

   Session = sessionmaker(bind=engine)
   session = Session()