from sqlalchemy import String, Integer, Date, DECIMAL, Boolean, JSON
import json
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class Movies(Base):
    __tablename__ = "movies"
    id: Mapped[str] = mapped_column(String(20), primary_key=True, unique=True)
    url: Mapped[str] = mapped_column(String(150), nullable=False)
    primaryTitle: Mapped[str] = mapped_column(String(100), nullable=False)
    type: Mapped[str] = mapped_column(String(20), nullable=False)
    description: Mapped[str] = mapped_column(String(500), nullable=False)
    primaryImage: Mapped[str] = mapped_column(String(200), nullable=False)
    contentRating: Mapped[str] = mapped_column(String(50), nullable=False)
    startYear: Mapped[int] = mapped_column(Integer(), nullable=False)
    endYear: Mapped[int] = mapped_column(Integer(), nullable=True)
    releaseDate: Mapped[Date] = mapped_column(Date, nullable=False)
    budget: Mapped[float] = mapped_column(DECIMAL(20, 2), nullable=False)
    grossWorldwide: Mapped[int] = mapped_column(DECIMAL(20, 2), nullable=False)
    averageRating: Mapped[float] = mapped_column(DECIMAL(10, 2), nullable=False)
    runtimeMinutes: Mapped[int] = mapped_column(Integer(), nullable=False)
    numVotes: Mapped[float] = mapped_column(DECIMAL(10, 2), nullable=False)
    isAdult: Mapped[bool] = mapped_column(Boolean(), nullable=False)
    genres: Mapped[json] = mapped_column(JSON(), nullable=True, default=[])
    interests: Mapped[json] = mapped_column(JSON(), nullable=True, default=[])
    countriesOfOrigin: Mapped[json] = mapped_column(JSON(), nullable=True, default=[])
    spokenLanguages: Mapped[json] = mapped_column(JSON(), nullable=True, default=[])
    filmingLocations: Mapped[json] = mapped_column(JSON(), nullable=True, default=[])
    productionCompanies: Mapped[json] = mapped_column(JSON(), nullable=True, default=[])
    externalLinks: Mapped[json] = mapped_column(JSON(), nullable=True, default=[])
