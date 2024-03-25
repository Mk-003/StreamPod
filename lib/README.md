Movie Database Seeder
This project seeds a SQLite database with fake movie, viewer, and comment data using SQLAlchemy and Faker.

#Setup
Install Dependencies: Make sure you have Python installed along with the required dependencies listed in requirements.txt. You can install them using pipenv:

pipenv install sqlalchemy alembic
pipenv shell

#database
data is stored in pod.db

#migrations
alembic init migrations


Database Setup: The project uses a SQLAlchemy database. 

bash
Copy code
python seeds.py
Usage
Seeder Script: seed_database.py contains the script to seed the database with fake data. You can adjust the number of movies, viewers, and comments generated by modifying the function arguments in the script.

CLI Interface: CLI.py provides a command-line interface to interact with the seeded database. You can perform various operations like finding all movies, viewers, comments, finding movies by ID or name, creating, updating, and deleting movies.

File Structure
modes.py: Defines the database models using SQLAlchemy ORM.
seeds.py: Script to seed the database with fake data.
CLI.py: Command-line interface for interacting with the database.
requirements.txt: List of project dependencies.
movies.db: SQLite database file.
README.md: Project README file.
Dependencies
SQLAlchemy: ORM library for database interaction.
Faker: Library for generating fake data.
argparse: Library for parsing command-line arguments.
Contributing
Contributions are welcome! If you find any issues or have suggestions for improvement, feel free to open an issue or create a pull request.
