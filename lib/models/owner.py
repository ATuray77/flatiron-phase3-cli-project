from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .base import Base

class Owner(Base):
    __tablename__ = "owners"
    id = Column(Integer, primary_key = True)
    username = Column(String, nullable=False )
    name = Column(String, nullable = False)
    phone= Column(String, nullable = False)
    email= Column(String, unique=True)

    cars = relationship("Car", backref="owner") # relationship

def __repr__(self):
    return f"\n<Owner" \
        + f"id={self.id}, " \
        + f"username={self.username}, " \
        + f"name={self.name}, " \
        + f"phone={self.phone}, " \
        + f"email={self.email}, " \
        + ">"