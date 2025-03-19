import web_scraper
import polars as pl


def transform_data():
    df = pl.DataFrame()
    data = web_scraper.fetch_top250_movies()

    df_request = pl.json_normalize(data)
    df = pl.concat([df, df_request])
    print(df.describe())
    df_polars = df.filter(~df.is_duplicated())
    df_polars.write_csv("../data/processed_data.csv")





