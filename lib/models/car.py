from sqlalchemy import Column, Integer, String, ForeignKey
from .base import Base

class Car(Base):
    __tablename__ = "cars"
    id = Column(Integer, primary_key = True)
    make = Column(String, nullable = False)
    model = Column(String, nullable = False)
    color = Column(String, nullable = False)
    owner_id = Column(Integer, ForeignKey("owners.id"))


    def __repr__(self):
        return f"\n<Car" \
            + f"id={self.id}, " \
            + f"make={self.make}, " \
            + f"model={self.model}, " \
            + f"color={self.color}, " \
            + ">"