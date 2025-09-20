from typing import List, Optional
from models.models import PlayerTeam, Station
from repositories.base import BaseRepository


class PlayerTeamRepository(BaseRepository):
    def __init__(self):
        super().__init__(PlayerTeam)

    async def create(self, **kwargs):
        return await super().create(**kwargs)

    async def get_all_with_user_station(self) -> List[PlayerTeam]:
        return await PlayerTeam.all().prefetch_related("user").all()

    async def get_by_id_with_user_station(
        self, id: int
    ) -> Optional[PlayerTeam]:
        return await PlayerTeam.filter(id=id).prefetch_related("user").first()

    async def add_score(self, id: int, score_to_add: int) -> tuple[int, int]:
        instance = await PlayerTeam.get_or_none(id=id)
        if instance:
            score = instance.score
            await instance.update_from_dict(
                {"score": score + score_to_add}
            ).save()
            # переход на следующую станцию
            await instance.update_from_dict(
                {"current_station": instance.current_station + 1}
            ).save()
            return instance.score, instance.current_station
        return None

    async def get_top_3_by_score(self) -> List[PlayerTeam]:
        return (
            await PlayerTeam.all()
            .order_by("-score")
            .limit(3)
            .prefetch_related("user")
        )

    async def set_current_station(
        self, id: int, station_number: int
    ) -> Optional[str]:
        team = await PlayerTeam.get_or_none(id=id)
        station = await Station.get_or_none(id=station_number)
        if team and station:
            team.update_from_dict({"current_station": station_number}).save()

        return station.name
