from models import Owner, Car

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from faker import Faker
#import requests
import random
#import json

fake = Faker()

engine = create_engine('sqlite:///parkingGarage.db')
Session = sessionmaker(bind=engine)  # enables communication with the db
session = Session()
if __name__ == '__main__':
    session.query(Owner).delete() # Reset DB
    session.query(Car).delete() # Reset DB
    session.commit()

# Use faker to seed 10 Users
owner_list = []
for _ in range(10):

    first_name=fake.first_name()
    last_name=fake.last_name()
    username = f"{first_name}_{last_name}"
    phone = fake.phone_number()

   
    owner = Owner(first_name=first_name, last_name=last_name, username = username, phone=phone, email = fake.ascii_email())
    
    session.add(owner)
    session.commit()
    owner_list.append(owner)
    
#print(owner_list)


makes_models = [
    "Toyota_Camry", 
    "Ford_Mustang", 
    "Cheverolet_Camaro", 
    "Honda_Pilot", 
    "Audi_A4", 
    "Hyundai_Elantra", 
    "Kia_Golf", 
    "Lexus_ES", 
    "BMW_X6", 
    "Teals_Model 3"
    ]
colors = ["white", "red", "green", "blue", "yellow", "purple", "brown", "pink", "grey", "black"]
# print(makes_models)
# print(colors)
cars_list = []
for i in range(10):
    car = Car(
        make_model = random.choice(makes_models),
        color = random.choice(colors),
        license_plate = fake.license_plate()
    )

    owner = random.choice(owner_list)
    owner.cars.append(car)
    cars_list.append(car)
    print(cars_list)

session.add_all(cars_list)
session.commit()




import ipdb; ipdb.set_trace()