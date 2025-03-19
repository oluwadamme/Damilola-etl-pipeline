from etl_pipeline.utils import config, utils
import requests


def fetch_top250_movies():
    url = config.RAPID_URL + "/top250-movies"

    headers = {
        "x-rapidapi-key": config.API_KEY,
        "x-rapidapi-host": config.RAPID_HOST
    }

    response = requests.get(url, headers=headers)

    movies = response.json()
    utils.write_to_file("../data/top_250_movies.json", movies)

    return movies


if __name__ == "__main__":
    fetch_top250_movies()
