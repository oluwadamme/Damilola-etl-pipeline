import polars as pl
from etl_pipeline.utils import utils
from model import Movies,Base


def load_data(df: pl.DataFrame):
    Session, engine = utils.connect_with_db()

    Base.metadata.create_all(engine)
    with Session.begin() as session:
        # Inserting data into tables
        for _, row in df.iter_rows():
            movie = session.query(Movies).filter_by(id=str(row["id"])).first()
            if not movie:
                _movie = Movies(
                    id=row["id"],
                    url=row["url"],
                    primaryTitle=row["primaryTitle"],
                    type=row["type"],
                    description=row["description"],
                    primaryImage=row["primaryImage"],
                    contentRating=row["contentRating"],
                    startYear=row["startYear"],
                    endYear=row["endYear"],
                    releaseDate=row["releaseDate"],
                    budget=row["budget"],
                    grossWorldwide=row["grossWorldwide"],
                    averageRating=row["averageRating"],
                    runtimeMinutes=row["runtimeMinutes"],
                    numVotes=row["numVotes"],
                    isAdult=row["isAdult"],
                )
                session.add(_movie)
        session.commit()

    pass
