from etl_pipeline.utils import config, utils
import requests
import logging


def fetch_top250_movies():
    try:
        url = config.RAPID_URL + "/top250-movies"

        headers = {
            "x-rapidapi-key": config.API_KEY,
            "x-rapidapi-host": config.RAPID_HOST,
        }

        response = requests.get(url, headers=headers)

        if response.status_code != 200:
            raise response.raise_for_status()

        movies = response.json()
        utils.write_to_file("../data/top_250_movies.json", movies)

        return movies
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        raise e


if __name__ == "__main__":
    fetch_top250_movies()
