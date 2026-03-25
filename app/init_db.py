from .engine import engine
from .base import Base

# IMPORTANT : importer les modèles
from .artiste import Artiste
from .instrument import Instrument


def init_db():
    Base.metadata.create_all(bind=engine)