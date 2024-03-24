from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from faker import Faker
from models import Base, Movie, Viewer, Comment



sessioncreator = sessionmaker(bind=engine)
mysession = sessioncreator()


fake = Faker()

if __name__=='__main__':

    for _ in range(40):
        movie = Movie(
            title=fake.catch_phrase(),
            genre=fake.word(),
            platform=fake.word(),
            price=fake.random_int(min=10, max=50)
        )
        mysession.add(movie)


    for _ in range(20):
        viewer = Viewer(
            name=fake.name()
        )
        mysession.add(viewer)
    
    mysession.commit()  #commit ensure 

        
