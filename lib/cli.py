import argparse
from modes import Movie, Viewer, Comment,Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Database connection
engine = create_engine('sqlite:///pod.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

def find_all_movies():
    movies = session.query(Movie).all()
    for movie in movies:
        print(movie)

def find_movie_by_id(movie_id):
    movie = session.query(Movie).filter_by(id=movie_id).first()
    if movie:
        print(movie)
    else:
        print("Movie not found.")

def find_movie_by_name(movie_name):
    movies = session.query(Movie).filter(Movie.title.ilike(f'%{movie_name}%')).all()
    if movies:
        for movie in movies:
            print(movie)
    else:
        print("No movies found with that name.")

def create_movie(title, genre, platform, price):
    movie = Movie(title=title, genre=genre, platform=platform, price=price)
    session.add(movie)
    session.commit()
    print("Movie created successfully.")

def update_movie(movie_id, **kwargs):
    movie = session.query(Movie).filter_by(id=movie_id).first()
    if movie:
        for key, value in kwargs.items():
            setattr(movie, key, value)
        session.commit()
        print("Movie updated successfully.")
    else:
        print("Movie not found.")

def delete_movie(movie_id):
    movie = session.query(Movie).filter_by(id=movie_id).first()
    if movie:
        session.delete(movie)
        session.commit()
        print("Movie deleted successfully.")
    else:
        print("Movie not found.")

def find_all_comments():
    comments = session.query(Comment).all()
    for comment in comments:
        print(comment)

def find_all_viewers():
    viewers = session.query(Viewer).all()
    for viewer in viewers:
        print(viewer)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Movie Viewer CLI")
    parser.add_argument("command", help="Command to execute")
    parser.add_argument("--id", type=int, help="Movie ID")
    parser.add_argument("--name", help="Movie name")
    parser.add_argument("--title", help="Movie title")
    parser.add_argument("--genre", help="Movie genre")
    parser.add_argument("--platform", help="Movie platform")
    parser.add_argument("--price", type=int, help="Movie price")

    args = parser.parse_args()

    if args.command == "find_all_movies":
        find_all_movies()
    elif args.command == "find_movie_by_id":
        find_movie_by_id(args.id)
    elif args.command == "find_movie_by_name":
        find_movie_by_name(args.name)
    elif args.command == "create_movie":
        create_movie(args.title, args.genre, args.platform, args.price)
    elif args.command == "update_movie":
        update_movie(args.id, title=args.title, genre=args.genre, platform=args.platform, price=args.price)
    elif args.command == "delete_movie":
        delete_movie(args.id)
    elif args.command == "find_all_comments":
        find_all_comments()
    elif args.command == "find_all_viewers":
        find_all_viewers()
    else:
        print("Invalid command.")
