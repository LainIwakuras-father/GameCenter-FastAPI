


from app.db.db import Base


class PlayerTeam(Base):
    __tablename__ = "tweet"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, index=True)
    user = relationship()
    teamname: Mapped[str] = mapped_column(String(100),nullable=True)
    score: Mapped[int] = mapped_column(nullable=True, default=0)
    stations: Mapped[List["StationOrder"]] = relationship()
    current_station: Mapped[int] = mapped_column(default=1)

    def __repr__(self):
        return f"{self.teamname}"
  
   