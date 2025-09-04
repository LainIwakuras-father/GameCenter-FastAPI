"""class tweet"""


class PlayerTeam(Base):
    __tablename__ = "tweet"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, index=True)
    points: Mapped[int] = mapped_column(

    )
    name: Mapped[str] = mapped_column(
        nullable=True,
    )
    description: Mapped[str] = mapped_column(
        nullable=True,
    )
    image: Mapped[str] = mapped_column(
        nullable=True,
    )
    assignment: Mapped[str] = mapped_column(
        nullable=True,
    )
    task: Mapped[str] = mapped_column(
        
    )
    created_at: Mapped[datetime] = mapped_column(
        server_default=func.now(),
        default=datetime.now(), nullable=True
    )