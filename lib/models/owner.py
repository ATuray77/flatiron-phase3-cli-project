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

    #testing 
    @classmethod
    def find_or_create_by(email):
        pass

    def __repr__(self):
        return f"\n<Owner" \
            + f"id={self.id}, " \
            + f"first_name={self.first_name}, " \
            + f"last_name={self.last_name}, " \
            + f"username={self.username}, " \
            + f"phone={self.phone}, " \
            + f"email={self.email}, " \
            + ">"