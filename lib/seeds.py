from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from faker import Faker
from modes import Base, Movie, Viewer, Comment

engine = create_engine('sqlite:///pod.db')
Base.metadata.create_all(engine)

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
    
    mysession.commit()  #commit ensure movie and viewer id are present

    for _ in range(50):
        comment = Comment(
            score=fake.random_int(min=1, max=10),
            content=fake.text(max_nb_chars=200),
            movie_id=fake.random_int(min=1, max=40),
            viewer_id=fake.random_int(min=15000, max=20000)
        )
        mysession.add(comment)
    
    mysession.commit()

print('All players Seeded, They should now be in your Database')

mysession.close()    

        
