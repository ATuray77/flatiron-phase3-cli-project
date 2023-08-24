from models import User, Car

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from faker import Faker
import random


engine = create_engine('sqlite:///parkingGarage.db')
Session = sessionmaker(bind=engine)  # enables communication with the db
session = Session()

session.query(User).delete() # Reset DB
session.query(Car).delete() # Reset DB
session.commit()