"""This is a boilerplate pipeline 'training' generated using Kedro 0.18.4."""

from kedro.pipeline import Pipeline, pipeline
from kedro.pipeline import node

from .nodes import user_item_matrix 
from .nodes import transpose_item_matrix 
from .nodes import aux_matrix_train_cf 
from .nodes import user_movies_vectors 
from .nodes import rec_size 
from .nodes import prediction_cf 
from .nodes import expand_cf_rec_list 
from .nodes import list_padding_cf 
from .nodes import fixed_cf_recs
from .nodes import output_cf 

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=user_item_matrix,
                inputs="rec_matrix",
                outputs="user_movies",
                name="user_item_matrix_node",
            ),
            node(
                func=transpose_item_matrix,
                inputs="movie_vector",
                outputs="movie_vector_t",
                name="transpose_item_matrix_node",
            ),
            node(
                func=aux_matrix_train_cf,
                inputs="rec_matrix",
                outputs="aux_matrix",
                name="aux_matrix_train_cf_node",
            ),
            node(
                func=user_movies_vectors,
                inputs=["rec_matrix", "movie_vector_t", "movie_vector"],
                outputs="user_movies",
                name="user_movies_vectors_node",
            ),
            node(
                func=rec_size,
                inputs=[],
                outputs="rec_size",
                name="rec_size_node",
            ),
           node(
                func=prediction_cf,
                inputs=["test_matrix", "rec_size", "user_movies"],
                outputs="recommended_cf",
                name="prediction_cf_node",
            ),
            node(
                func=expand_cf_rec_list,
                inputs="recommended_cf",
                outputs="max_length",
                name="expand_cf_rec_list_node",
            ),
            node(
                func=list_padding_cf,
                inputs=["recommended_cf", "max_length"],
                outputs="recommended_cf",
                name="list_padding_cf_node",
            ),
            node(
                func=fixed_cf_recs,
                inputs=["recommended_cf", "movies"],
                outputs="rec_cf",
                name="fixed_cf_recs_node",
            ),
            node(
                func=output_cf,
                inputs="rec_cf",
                outputs="rec_cf",
                name="expand_cf_rec_list_node",
            ),
    ]
    )
