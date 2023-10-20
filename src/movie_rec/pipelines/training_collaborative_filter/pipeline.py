"""This is a boilerplate pipeline 'training' generated using Kedro 0.18.4."""

from kedro.pipeline import Pipeline, pipeline
from kedro.pipeline import node

from .nodes import factors 
from .nodes import svd_matrixes 
from .nodes import user_item_matrix 
from .nodes import transpose_item_matrix 
from .nodes import aux_matrix_train_cf 
from .nodes import user_movies_vectors 
from .nodes import rec_size 
from .nodes import prediction_cf 
from .nodes import expand_cf_rec_list 
from .nodes import list_padding_cf
from .nodes import convert_cf_df
from .nodes import fixed_cf_recs
from .nodes import output_cf 

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=factors,
                inputs=[],
                outputs="factors",
                name="factors_node",
            ),
            node(
                func=svd_matrixes,
                inputs=["factors", "rec_matrix"],
                outputs=["user_vector", "eingenvalues", "movie_vector"],
                name="svd_matrixes_node",
            ),
            node(
                func=user_item_matrix,
                inputs="rec_matrix",
                outputs="user_movies_empty",
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
                inputs=["rec_matrix", "movie_vector_t"],
                outputs="aux_matrix",
                name="aux_matrix_train_cf_node",
            ),
            node(
                func=user_movies_vectors,
                inputs=["aux_matrix", "rec_matrix", "movie_vector_t", "movie_vector"],
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
                inputs=["rec_size", "test_matrix", "user_movies"],
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
                outputs="recommended_cf_padded",
                name="list_padding_cf_node",
            ),
            node(
                func=convert_cf_df,
                inputs="recommended_cf_padded",
                outputs="recommended_cf_df",
                name="convert_cf_df_node",
            ),
            node(
                func=fixed_cf_recs,
                inputs=["recommended_cf_df", "movies"],
                outputs="rec_cf",
                name="fixed_cf_recs_node",
            ),
            node(
                func=output_cf,
                inputs="rec_cf",
                outputs="rec_cf_output",
                name="output_cf_node",
            ),
    ]
    )
