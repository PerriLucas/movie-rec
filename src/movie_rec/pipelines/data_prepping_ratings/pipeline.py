"""This is a boilerplate pipeline 'feature_engineering' generated using Kedro
0.18.4."""

from kedro.pipeline import Pipeline, pipeline

# from kedro.pipeline import node


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=ratings_raw_data_get,
                inputs="ratings_raw_data_get",
                outputs="ratings",
                name="ratings_raw_data_get_node",
            ),
            node(
                func=drop_timestamp,
                inputs="ratings",
                outputs="ratings",
                name="drop_timestamp_node",
            ),
            node(
                func=filter_out_movies_no_genre,
                inputs="ratings",
                outputs="ratings",
                name="filter_out_movies_no_genre_node",
            ),
            node(
                func=movies_with_ratings,
                inputs="ratings",
                outputs="movies_with_ratings",
                name="movies_with_ratings_node",
            ),
            node(
                func=pivot_ratings,
                inputs="ratings",
                outputs="pivoted_ratings",
                name="pivot_ratings_node",
            ),
           node(
                func=filtered_pivoted_ratings,
                inputs="pivoted_ratings",
                outputs="pivoted_ratings",
                name="filtered_pivoted_ratings_node",
            ),
            node(
                func=create_total_ratings,
                inputs="filtered_pivoted_ratings",
                outputs="pivoted_ratings",
                name="create_total_ratings_node",
            ),
            node(
                func=ratingless_users,
                inputs="pivoted_ratings",
                outputs="total_ratings_in",
                name="ratingless_users_node",
            ),
            node(
                func=final_ratings,
                inputs="final_ratings",
                outputs="final_ratings",
                name="final_ratings_node",
            ),
    ]
    )
