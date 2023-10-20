from kedro.pipeline import Pipeline, pipeline
from kedro.pipeline import node

from .nodes import user_feature_matrix 
from .nodes import cosine_similarity_prediction 
from .nodes import rec_size 
from .nodes import user_recommendation 
from .nodes import expand_cb_rec_list 
from .nodes import list_padding_cb 
from .nodes import convert_cb_df 
from .nodes import fixed_cb_recs 
from .nodes import output_cb 

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=user_feature_matrix,
                inputs=["user_feature_empty", "len_rec_matrix", "rec_matrix", "aux_matrix_train"],
                outputs=["user_feature", "user_feature_df"],
                name="user_feature_matrix_node",
            ),
            node(
                func=cosine_similarity_prediction,
                inputs=["user_feature", "final_movies_matrix"],
                outputs=["prediction", "prediction_df"],
                name="cosine_similarity_prediction_node",
            ),
            node(
                func=rec_size,
                inputs=[],
                outputs="rec_size",
                name="rec_size_node",
            ),
            node(
                func=user_recommendation,
                inputs=["test_matrix", "rec_size", "prediction"], 
                outputs="recommendation",
                name="user_recommendation_node",
            ),
            node(
                func=expand_cb_rec_list,
                inputs="recommendation",
                outputs="max_length_cb",
                name="expand_cb_rec_list_node",
            ),
            node(
                func=list_padding_cb,
                inputs=["recommendation", "max_length_cb"],
                outputs="recommendation_padded",
                name="list_padding_cb_node",
            ),
            node(
                func=convert_cb_df,
                inputs="recommendation_padded",
                outputs="recommendations_df",
                name="convert_cb_df_node",
            ),
            node(
                func=fixed_cb_recs,
                inputs=["recommendations_df", "movies"],
                outputs="rec_cb",
                name="fixed_cb_recs_node",
            ),
            node(
                func=output_cb,
                inputs="rec_cb",
                outputs="rec_cb_output",
                name="output_cb",
            ),
    ]
    )
