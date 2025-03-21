import json
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import logging
import psycopg2

from etl_pipeline.utils.config import DATABASE_URL


def write_to_file(path: str, data):
    try:
        with open(path, "w") as json_file:
            json.dump(data, json_file, indent=4)
        logging.log(level=1, msg=f"Data successfully written to {path}")
    except IOError as e:
        logging.error(f"I/O error: {e}")
    except Exception as e:
        logging.error(f"Unexpected error: {e}")


def connect_with_db():
    try:
        engine = create_engine(DATABASE_URL)
        Session = sessionmaker(bind=engine)
        return Session, engine
    except Exception as e:
        logging.error(f"Database connection error: {str(e)}")
        return None, None
