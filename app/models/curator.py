from typing import Optional
from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import  Mapped, mapped_column, relationship

from app.db.db import Base
from app.models.station import Station
from app.models.user import User




class Curator(Base):
    __tablename__ = "curators"
    
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    station_id: Mapped[Optional[int]] = mapped_column(ForeignKey("stations.id"), nullable=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), unique=True)
    name: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    
    # Relationships
    station: Mapped[Optional["Station"]] = relationship()
    user: Mapped["User"] = relationship(back_populates="curator")

    def __repr__(self):
        return f"{self.name} " 