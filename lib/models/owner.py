from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .base import Base
from .session import session

class Owner(Base):
    __tablename__ = "owners"
    id = Column(Integer, primary_key = True)
    first_name = Column(String, nullable= False)
    last_name = Column(String, nullable= False)
    username = Column(String, unique=True, nullable=False )
    phone= Column(String, nullable = False)
    email= Column(String, unique=True)

    cars = relationship("Car", backref="owner") # relationship

    #creating get_owner_cars
    @classmethod
    def find_my_cars(cls, email):
        owner = session.query(cls).filter(cls.email.like(email)).first()
        if owner is None:
            print(f"No owner found with that email")
        else:
            print(f"Cars owned by {owner.first_name} {owner.last_name}:")
            for car in owner.cars:
                print(f"{car.make_model}, {car.color}, {car.license_plate}")
    #creating get_owner_cars
    @classmethod
    def find_or_create_by(cls, email):
        owner = session.query(cls).filter(cls.email.like(email)).first()
        if owner:
            return owner
        else:
            owner = Owner(email=email)
            session.add(owner)
            session.commit()
            return owner


        #import ipdb; ipdb.set_trace()

        

    def __repr__(self):
        return f"\n<Owner" \
            + f"id={self.id}, " \
            + f"first_name={self.first_name}, " \
            + f"last_name={self.last_name}, " \
            + f"username={self.username}, " \
            + f"phone={self.phone}, " \
            + f"email={self.email}, " \
            + ">"