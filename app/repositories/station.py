from app.models.station import Station
from app.repositories.base import BaseRepository


class StationRepository(BaseRepository):
    def __init__(self):
        super().__init__(Station)