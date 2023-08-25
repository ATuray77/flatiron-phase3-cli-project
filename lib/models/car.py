from sqlalchemy import Column, Integer, String, ForeignKey
from .base import Base

class Car(Base):
    __tablename__ = "cars"
    id = Column(Integer, primary_key = True)
    make_model = Column(String, nullable = False)
    color = Column(String, nullable = False)
    license_plate = Column(String, nullable=False)
    owner_id = Column(Integer, ForeignKey("owners.id"))


    def __repr__(self):
        return f"\n<Car" \
            + f"id={self.id}, " \
            + f"make_model={self.make_model}, " \
            + f"color={self.color}, " \
            + f"license_plate={self.license_plate}, " \
            + ">"