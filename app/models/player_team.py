from typing import List
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.station_order import StationOrder
from app.models.user import User
from app.db.db import Base


class PlayerTeam(Base):
    __tablename__ = "player_teams"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, index=True)
    teamname: Mapped[str] = mapped_column(String(100),nullable=True)
    score: Mapped[int] = mapped_column(nullable=True, default=0)
    current_station: Mapped[int] = mapped_column(default=1)
 

    # one to many relationship
    stations: Mapped[List["StationOrder"]] = relationship("StationOrder", back_populates="player_teams")
    # one to one relationship
    user: Mapped["User"] = relationship("User", ack_populates="player_team")
    def __repr__(self):
        return f"{self.teamname}"
  
   