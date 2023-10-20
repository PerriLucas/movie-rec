from kedro.pipeline import Pipeline, pipeline
from kedro.pipeline import node

from .nodes import generate_training_ratings 
from .nodes import generate_feature_matrix 
from .nodes import transfom_genre_list 
from .nodes import generate_empty_matrix 
from .nodes import aux_matrix 
from .nodes import test_matrix 


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=generate_training_ratings,
                inputs="training_sample",
                outputs=["rec_matrix", "rec_matrix_txt"],
                name="generate_training_ratings_node",
            ),
            node(
                func=generate_feature_matrix,
                inputs="final_movies_fixed",
                outputs=["final_movies_matrix", "final_movies_matrix_df"],
                name="generate_feature_matrix_node",
            ),
            node(
                func=transfom_genre_list,
                inputs="unique_genres",
                outputs="unique_genres_list",
                name="transfom_genre_list_node",
            ),
            node(
                func=generate_empty_matrix,
                inputs=["unique_genres_list", "rec_matrix"],
                outputs=["user_feature_empty", "user_feature_empty_df", "len_rec_matrix"],
                name="generate_empty_matrix_node",
            ),
            node(
                func=aux_matrix,
                inputs=["rec_matrix", "final_movies_matrix"],
                outputs=["aux_matrix_train", "aux_matrix_train_df"],
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

