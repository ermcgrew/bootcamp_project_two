# Python SQL toolkit and Object Relational Mapper
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, inspect

# create engine to hawaii.sqlite
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(engine, reflect=True)

# View all of the classes that automap found
Base.classes.keys()

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(bind=engine)


#use inspector to see columns names and types for each table
inspector = inspect(engine)

print("Measurement:")
columns = inspector.get_columns('measurement')
for column in columns:
    print(column['name'], column['type'])

print("\nStation:")
columns = inspector.get_columns('station')
for column in columns:
    print(column['name'], column['type'])