import web_scraper
import polars as pl


def transform_data(api_data) -> pl.DataFrame:
    df = pl.DataFrame()

    df_request = pl.json_normalize(data)
    df = pl.concat([df, df_request])
    df_polars = df.filter(~df.is_duplicated())
    df_polars = df_polars.drop(
        ["originalTitle", "interests", "countriesOfOrigin", "externalLinks", "spokenLanguages", "filmingLocations",
         "productionCompanies", "genres"])
    df_polars.write_csv("../data/processed_data.csv")
    return df_polars


if __name__ == "__main__":
    data = web_scraper.fetch_top250_movies()
    transform_data(data)
