from kedro.pipeline import Pipeline, pipeline
from kedro.pipeline import node

from .nodes import final_movie_filter 
from .nodes import final_movie_matrix 
from .nodes import grouped_population 
from .nodes import stratify_dataset 
from .nodes import prepare_test_df 
from .nodes import prepare_train_df 



def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=final_movie_filter,
                inputs=["movies_titleless", "movies_with_ratings"],
                outputs="final_movies",
                name="final_movie_filter_node",
            ),
            node(
                func=final_movie_matrix,
                inputs="final_movies",
                outputs="final_movies_fixed",
                name="final_movie_matrix_node",
            ),
            node(
                func=grouped_population,
                inputs="total_ratings_in",
                outputs="grouped_ratings",
                name="grouped_population_node",
            ),
            node(
                func=stratify_dataset,
                inputs=["grouped_ratings"],
                outputs=["train_df", "stratified_sample"],
                name="stratify_dataset_node",
            ),
            node(
                func=prepare_test_df,
                inputs="stratified_sample",
                outputs="test_df",
                name="prepare_test_df_node",
            ),
           node(
                func=prepare_train_df,
                inputs="train_df",
                outputs=["training_sample", "train_df_df"],
                name="prepare_train_df",
            ),
    ]
    )

