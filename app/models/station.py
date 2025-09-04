from sqlalchemy import ForeignKey, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from app.db.db import Base

"""class Станций"""


class Station(Base):
    __tablename__ = "stations"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, index=True)
    time: Mapped[str] = mapped_column()
    points: Mapped[int] = mapped_column(nullable=True)
    name: Mapped[str] = mapped_column(String(100),nullable=True,)
    description: Mapped[str] = mapped_column(Text,nullable=True)
    image: Mapped[str] = mapped_column(String(255),nullable=True)
    assignment: Mapped[str] = mapped_column(Text,nullable=True,)
    task: Mapped[str] = mapped_column(ForeignKey("tasks.id"),nullable=True)
  
    def __repr__(self):
        return f"{self.name}"