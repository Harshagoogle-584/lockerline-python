
from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from lockerline.db import Base


class Tower(Base):
    __tablename__ = "towers"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    code: Mapped[str] = mapped_column(String(8), unique=True)
    name: Mapped[str] = mapped_column(String(80))


class Door(Base):
    __tablename__ = "doors"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    tower_id: Mapped[int] = mapped_column(ForeignKey("towers.id"))

    no: Mapped[str] = mapped_column(String(8), nullable=False)
    size_class: Mapped[str] = mapped_column(String(1), nullable=False)            # S | M | L
    current_parcel_id: Mapped[int | None] = mapped_column(Integer, nullable=True)


class Resident(Base):
    __tablename__ = "residents"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    tower_id: Mapped[int] = mapped_column(ForeignKey("towers.id"))

    flat: Mapped[str] = mapped_column(String(8))
    name: Mapped[str] = mapped_column(String(80))
