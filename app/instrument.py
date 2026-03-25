from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from .base import Base


class Instrument(Base):
    __tablename__ = "instrument"

    id_instrument = Column(Integer, primary_key=True, autoincrement=True)
    nom = Column(String(100), nullable=False, unique=True)

    artistes = relationship("Artiste", back_populates="instrument")    