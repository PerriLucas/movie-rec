from kedro.pipeline import Pipeline, pipeline
from kedro.pipeline import node

from .nodes import ratings_raw_data_get 
from .nodes import drop_timestamp 
from .nodes import filter_out_movies_no_genre 
from .nodes import movies_with_ratings 
from .nodes import pivot_ratings
from .nodes import remove_outliers
from .nodes import create_total_ratings
from .nodes import ratingless_users 
from .nodes import final_ratings 


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=ratings_raw_data_get,
                inputs=[],
                outputs="ratings",
                name="ratings_raw_data_get_node",
            ),
            node(
                func=drop_timestamp,
                inputs="ratings",
                outputs="ratings_no_tmstp",
                name="drop_timestamp_node",
            ),
            node(
                func=filter_out_movies_no_genre,
                inputs=["ratings_no_tmstp", "movie_with_genres"],
                outputs="ratings_filtered",
                name="filter_out_movies_no_genre_node",
            ),
            node(
                func=movies_with_ratings,
                inputs="ratings_filtered",
                outputs="movies_with_ratings",
                name="movies_with_ratings_node",
            ),
            node(
                func=pivot_ratings,
                inputs="ratings_filtered",
                outputs="pivoted_ratings",
                name="pivot_ratings_node",
            ),
           node(
                func=remove_outliers,
                inputs="pivoted_ratings",
                outputs="filtered_pivoted_ratings",
                name="remove_outliers_node",
            ),
            node(
                func=create_total_ratings,
                inputs="pivoted_ratings",
                outputs="ratings_total",
                name="create_total_ratings_node",
            ),
            node(
                func=ratingless_users,
                inputs="ratings_total",
                outputs="total_ratings_in",
                name="ratingless_users_node",
            ),
            node(
                func=final_ratings,
                inputs="ratings_total",
                outputs="final_ratings",
                name="final_ratings_node",
            ),
    ]
    )
