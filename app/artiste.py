from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from .base import Base


class Artiste(Base):
    __tablename__ = "artiste"

    id_artiste = Column(Integer, primary_key=True, autoincrement=True)
    nom = Column(String(100), nullable=False)
    instrument_id = Column(Integer, ForeignKey("instrument.id_instrument"), nullable=True)

    instrument = relationship("Instrument", back_populates="artistes")
