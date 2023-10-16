"""This is a boilerplate pipeline 'serving' generated using Kedro 0.18.4."""

from kedro.pipeline import Pipeline, pipeline

# from kedro.pipeline import node


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=generate_training_ratings,
                inputs="train_df",
                outputs="rec_matrix",
                name="generate_training_ratings_node",
            ),
            node(
                func=generate_feature_matrix,
                inputs="final_movies",
                outputs="final_movies_matrix",
                name="generate_feature_matrix_node",
            ),
            node(
                func=transfom_genre_list,
                inputs="unique_genres",
                outputs="unique_genres",
                name="transfom_genre_list_node",
            ),
            node(
                func=generate_empty_matrix,
                inputs=["unique_genres", "rec_matrix"],
                outputs="user_feature",
                name="generate_empty_matrix_node",
            ),
            node(
                func=aux_matrix,
                inputs=["rec_matrix", "final_movies_matrix"],
                outputs="aux_matrix_train",
                name="aux_matrix_node",
            ),
           node(
                func=test_matrix,
                inputs="test_df",
                outputs="test_matrix",
                name="test_matrix_node",
            ),
    ]
    )

