import polars as pl


def transform_data(api_data) -> pl.DataFrame:
    df = pl.DataFrame()

    df_request = pl.json_normalize(api_data)
    df = pl.concat([df, df_request])
    df_polars = df.filter(~df.is_duplicated())
    df_polars_without_null = df_polars.with_columns(
        df_polars["budget"].fill_null(0),
        df_polars["grossWorldwide"].fill_null(0),
        df_polars["runtimeMinutes"].fill_null(0),
        df_polars["averageRating"].fill_null(0),
        df_polars["numVotes"].fill_null(0),
        df_polars["contentRating"].fill_null(""),
        df_polars["interests"].fill_null([]),
        df_polars["countriesOfOrigin"].fill_null([]),
        df_polars["externalLinks"].fill_null([]),
        df_polars["spokenLanguages"].fill_null([]),
        df_polars["filmingLocations"].fill_null([]),
        df_polars["productionCompanies"].fill_null([]),
        df_polars["genres"].fill_null([]),
    )
    df_polars_without_null.write_parquet("data/processed_data.parquet")
    return df_polars_without_null
