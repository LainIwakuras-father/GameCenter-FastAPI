from app.models.station import Station
from app.repositories.base import BaseRepository


class StationRepository(BaseRepository):
    def __init__(self):
        super().__init__(Station)

    async def get_all_with_tasks(self):
        return await Station.all().prefetch_related("task").all()