from models import Owner, Car

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from faker import Faker
import random

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

#  first_name 
#     last_name
#     username 
#     phone
#     email

