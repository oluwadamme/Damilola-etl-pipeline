from etl_pipeline.src import web_scraper, data_transform, db_loader


def run_etl_pipeline():
    data = web_scraper.fetch_top250_movies()
    df_polars = data_transform.transform_data(data)
    db_loader.load_data(df_polars)
