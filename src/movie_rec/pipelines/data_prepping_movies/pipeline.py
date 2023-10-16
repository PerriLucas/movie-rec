from kedro.pipeline import Pipeline, pipeline
from kedro.pipeline import node

from .nodes import movie_raw_data_get 
from .nodes import list_unique_genres 
from .nodes import turn_values_into_columns 
from .nodes import fix_columns_movies 
from .nodes import filter_out_non_genre 
from .nodes import remove_non_genre_column 
from .nodes import titleless_movies 
from .nodes import list_movies_with_genre 

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=movie_raw_data_get,
                inputs=[],
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
                outputs="movies_pivoted",
                name="turn_values_into_columns_node",
            ),
            node(
                func=fix_columns_movies,
                inputs="movies_pivoted",
                outputs="movies_fixed",
                name="fix_columns_movies_node",
            ), 
            node(
                func=filter_out_non_genre,
                inputs="movies_fixed",
                outputs="movies_usable_genres",
                name="filter_out_non_genre_node",
            ),
            node(
                func=remove_non_genre_column,
                inputs="movies_usable_genres",
                outputs="movies_removed_column",
                name="remove_non_genre_column_node",
            ),
            node(
                func=titleless_movies,
                inputs="movies_removed_column",
                outputs="movies_titleless",
                name="titleless_movies_node",
            ),
            node(
                func=list_movies_with_genre,
                inputs="movies_removed_column",
                outputs="movie_with_genres",
                name="list_movies_with_genre_node",
            ),
    ]
    )
