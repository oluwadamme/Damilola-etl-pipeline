import polars as pl


def transform_data(api_data) -> pl.DataFrame:
    df = pl.DataFrame()

    df_request = pl.json_normalize(api_data)
    df = pl.concat([df, df_request])
    df_polars = df.filter(~df.is_duplicated())
    df_polars = df_polars.drop(
        [
            "originalTitle",
            "interests",
            "countriesOfOrigin",
            "externalLinks",
            "spokenLanguages",
            "filmingLocations",
            "productionCompanies",
            "genres",
        ]
    )
    df_polars_without_null = df_polars.with_columns(
        df_polars["budget"].fill_null(0),
        df_polars["grossWorldwide"].fill_null(0),
        df_polars["runtimeMinutes"].fill_null(0),
        df_polars["averageRating"].fill_null(0),
        df_polars["numVotes"].fill_null(0),
        df_polars["contentRating"].fill_null(""),
    )
    df_polars_without_null.write_csv("data/processed_data.csv")
    return df_polars_without_null
