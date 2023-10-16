"""This is a boilerplate pipeline 'feature_engineering' generated using Kedro
0.18.4."""

from kedro.pipeline import Pipeline, pipeline

# from kedro.pipeline import node


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=final_movie_filter,
                inputs="movies_titleless",
                outputs="final_movies",
                name="final_movie_filter_node",
            ),
            node(
                func=final_movie_matrix,
                inputs="final_movies",
                outputs="final_movies",
                name="final_movie_matrix_node",
            ),
            node(
                func=grouped_population,
                inputs="total_ratings_in",
                outputs="total_ratings_in",
                name="grouped_population_node",
            ),
            node(
                func=stratify_dataset,
                inputs="total_ratings_in",
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
                outputs="train_df",
                name="prepare_train_df",
            ),
    ]
    )

