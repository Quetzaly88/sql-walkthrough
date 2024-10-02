# from sqlalchemy import (
#     create_engine, Column, Integer, String
# )
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker


# # executing the instructions from the "chinook" database
# db = create_engine("postgresql:///chinook")
# base = declarative_base()


# # create a class-based model for the "Programmer" table
# class Programmer(base):
#     __tablename__ = "Programmer"
#     id = Column(Integer, primary_key=True)
#     first_name = Column(String)
#     last_name = Column(String)
#     gender = Column(String)
#     nationality = Column(String)
#     famous_for = Column(String)


# # instead of connecting to the database directly, we will ask for a session
# # create a new instance of sessionmaker, then point to our engine (the db)
# Session = sessionmaker(db)
# # opens an actual session by calling the Session() subclass defined above
# session = Session()

# # creating the database using declarative_base subclass
# base.metadata.create_all(db)


# # creating records on our Progammer table
# ada_lovelace = Programmer(
#     first_name="Ada",
#     last_name="Lovelace",
#     gender="F",
#     nationality="British",
#     famous_for="First Programmer"
# )

# alan_turing = Programmer(
#     first_name="Alan",
#     last_name="Turing",
#     gender="M",
#     nationality="British",
#     famous_for="Modern Computing"
# )

# grace_hopper = Programmer(
#     first_name="Grace",
#     last_name="Hopper",
#     gender="F",
#     nationality="American",
#     famous_for="COBOL language"
# )

# margaret_hamilton = Programmer(
#     first_name="Margaret",
#     last_name="Hamilton",
#     gender="F",
#     nationality="American",
#     famous_for="Apollo 11"
# )

# bill_gates = Programmer(
#     first_name="Bill",
#     last_name="Gates",
#     gender="M",
#     nationality="American",
#     famous_for="Microsoft"
# )

# tim_berners_lee = Programmer(
#     first_name="Tim",
#     last_name="Berners-Lee",
#     gender="M",
#     nationality="British",
#     famous_for="World Wide Web"
# )

# andrea_li = Programmer(
#     first_name="Andrea",
#     last_name="Andrea_Li",
#     gender="F",
#     nationality="American",
#     famous_for="Trying hard"
# )

# # add each instance of our programmers to our session
# # session.add(ada_lovelace)
# # session.add(alan_turing)
# # session.add(grace_hopper)
# # session.add(margaret_hamilton)
# # session.add(bill_gates)
# # session.add(tim_berners_lee)
# # session.add(andrea_li)


# # #updating a single record
# # programmer = session.query(Programmer).filter_by(id=7).first()
# # programmer.famous_for = "World President"


# # # commit our session to the database
# # session.commit()

# # # update multiple records
# # people = session.query(Programmer)
# # for person in people:
# #     if person.gender == "F":
# #         person.gender = "Female"
# #     elif person.gender == "M":
# #         person.gender = "Male"
# #     else:
# #         print("Gender not defined")
# #     session.commit()


# # # deleting a single record
# # fname = input("Enter a first name: ")
# # lname = input("Enter a last name: ")
# # programmer = session.query(Programmer).filter_by(first_name=fname, last_name=lname).first()
# # # defensive programming
# # if programmer is not None:
# #     print("Programmer found: ", programmer.first_name + " " + programmer.last_name)
# #     confirmation = input("Are you sure you want to delete this record? (y/n) ")
# #     if confirmation.lower() == "y":
# #         session.delete(programmer)
# #         session.commit()
# #         print("Programmer has been deleted")
# #     else:
# #         print("Programmer not deleted")
# # else:
# #     print("No records found")



# # query the database to find all Programmers
# programmers = session.query(Programmer)
# for programmer in programmers:
#     print(
#         programmer.id,
#         programmer.first_name + " " + programmer.last_name,
#         programmer.gender,
#         programmer.nationality,
#         programmer.famous_for,
#         sep=" | "
#     )


from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Set up the connection to the PostgreSQL database
# Ensure the driver (`psycopg2` in this case) matches your environment
db = create_engine("postgresql+psycopg2://username:password@localhost:5432/chinook")

# Create a base class for the models to inherit from
base = declarative_base()

# Create a class-based model for the "FavouritePlaces" table
class FavouritePlaces(base):
    __tablename__ = "FavouritePlaces"  # The name of the table in the database

    # Define the columns of the table
    id = Column(Integer, primary_key=True)  # Primary key column
    country_name = Column(String, nullable=False)  # Country name (cannot be null)
    capital_city = Column(String, nullable=False)  # Capital city (cannot be null)
    population = Column(Float)  # Population of the place (in millions)
    area = Column(Float)  # Area in square kilometers
    description = Column(String)  # Short description of the place

# Instead of directly connecting to the database, use sessionmaker to manage sessions
Session = sessionmaker(bind=db)
session = Session()  # Create an instance of the session to interact with the database

# Create the database and the FavouritePlaces table if it doesn't already exist
base.metadata.create_all(db)

# Adding records to the FavouritePlaces table

# Create an instance for Paris
paris = FavouritePlaces(
    country_name="France",
    capital_city="Paris",
    population=11.1,  # Population in millions
    area=105.4,  # Area in square kilometers
    description="Known for the Eiffel Tower and rich cultural history."
)

# Create an instance for Tokyo
tokyo = FavouritePlaces(
    country_name="Japan",
    capital_city="Tokyo",
    population=37.4,  # Population in millions
    area=2194,  # Area in square kilometers
    description="World's most populous metropolitan area, famous for its technology and culture."
)

# Create an instance for New York City
new_york = FavouritePlaces(
    country_name="USA",
    capital_city="New York City",
    population=8.4,  # Population in millions
    area=783.8,  # Area in square kilometers
    description="The largest city in the USA, famous for the Statue of Liberty and Times Square."
)

# Add these records to the session
session.add(paris)
session.add(tokyo)
session.add(new_york)

# Commit the changes to the database to persist the added records
session.commit()

# Querying the database to list all favourite places
favourite_places = session.query(FavouritePlaces).all()  # Retrieve all records from FavouritePlaces
for place in favourite_places:
    # Print details for each place
    print(
        place.id,  # Unique identifier
        place.country_name,  # Country name
        place.capital_city,  # Capital city
        place.population,  # Population in millions
        place.area,  # Area in square kilometers
        place.description,  # Short description
        sep=" | "  # Separator for better readability
    )
