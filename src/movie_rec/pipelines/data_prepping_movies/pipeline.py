"""This is a boilerplate pipeline 'feature_engineering' generated using Kedro
0.18.4."""

from kedro.pipeline import Pipeline, pipeline

# from kedro.pipeline import node


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=movie_raw_data_get,
                inputs="movies_raw_data_get",
                outputs="movies",
                name="movie_raw_data_get_node",
            ),
            node(
                func=list_unique_genres,
                inputs="movies",
                outputs="unique_genres",
                name="list_unique_genres_node",
            ),
            node(
                func=turn_values_into_columns,
                inputs=["unique_genres", "movies"],
                outputs="movies",
                name="turn_values_into_columns_node",
            ),
            node(
                func=fix_columns_movies,
                inputs="movies",
                outputs="movies",
                name="fix_columns_movies_node",
            ), 
            node(
                func=filter_out_non_genre,
                inputs="movies",
                outputs="movies",
                name="filter_out_non_genre_node",
            ),
            node(
                func=remove_non_genre_column,
                inputs="movies",
                outputs="movies",
                name="remove_non_genre_column_node",
            ),
            node(
                func=titleless_movies,
                inputs="movies",
                outputs="movies_titleless",
                name="titleless_movies_node",
            ),
            node(
                func=list_movies_with_genre,
                inputs="movies",
                outputs="movie_with_genres",
                name="list_movies_with_genre_node",
            ),
    ]
    )
