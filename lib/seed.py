from models import Owner, Car

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from faker import Faker
import requests
import random
import json

fake = Faker()

engine = create_engine('sqlite:///parkingGarage.db')
Session = sessionmaker(bind=engine)  # enables communication with the db
session = Session()

session.query(Owner).delete() # Reset DB
session.query(Car).delete() # Reset DB
session.commit()

# Use faker to seed 10 Users
for _ in range(10):

    first_name=fake.first_name()
    last_name=fake.last_name()
    username = f"{first_name}_{last_name}"
    phone = fake.phone_number()


    owner = Owner(first_name=first_name, last_name=last_name, username = username, phone=phone, email = fake.ascii_email())
    print(owner)
    session.add(owner)
    session.commit()


cars = []
makes_models = [
    ("Toyota", "Camry"), 
    ("Ford", "Mustang"), 
    ("Cheverolet", "Camaro"), 
    ("Honda", "Pilot"), 
    ("Audi", "A4"), 
    ("Hyundai", "Elantra"), 
    ("Kia", "Golf"), 
    ("Lexus", "ES"), 
    ("BMW", "X6"), 
    ("Teals", "Model 3")
]
color = ["white", "red", "green", "blue", "yellow", "purple", "brown", "pink", "grey", "black"]



    # make 
    # model
    # color 
    # license_plate


    #import ipdb; ipdb.set_trace()