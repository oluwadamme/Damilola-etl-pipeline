from etl_pipeline.src import web_scraper, data_transform, db_loader


def run_etl_pipeline():
    print("fetching...")
    data = web_scraper.fetch_top250_movies()
    print("transforming")
    df_polars = data_transform.transform_data(data)
    print("loading to db")
    db_loader.load_data(df_polars)


if __name__ == "__main__":
    run_etl_pipeline()
