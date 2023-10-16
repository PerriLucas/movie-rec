"""Project pipelines."""
from typing import Dict

from kedro.pipeline import Pipeline

from kedro.framework.project import find_pipelines

from movie_rec.pipelines import (
    data_prepping_movies,
    data_prepping_ratings,
    test_and_training_split,
    matrix_generation,
    training_content_based,
    training_collaborative_filter,
)


def register_pipelines() -> Dict[str, Pipeline]:
    """Register the project's pipelines.

    Returns:
        A mapping from pipeline names to ``Pipeline`` objects.
    """
    data_prepping_movies_pipeline = data_prepping_movies.create_pipeline()
    data_prepping_ratings_pipeline = data_prepping_ratings.create_pipeline()
    test_and_training_split_pipeline = test_and_training_split.create_pipeline()
    matrix_generation_pipeline = matrix_generation.create_pipeline()
    training_content_based_pipeline = training_content_based.create_pipeline()
    training_collaborative_filter_pipeline = training_collaborative_filter.create_pipeline()

    # Leaving this commented as it is a new feature and could be useful eventually
    # As of today, I'm against running everything by default.
    # pipelines = find_pipelines()
    # pipelines["__default__"] = sum(pipelines.values())

    return {
        "content_based_pipeline" : (
            data_prepping_movies_pipeline,
            data_prepping_ratings_pipeline,
            test_and_training_split_pipeline,
            matrix_generation_pipeline,
            training_content_based_pipeline
        )
        , "collaborative_filter_pipeline" : (
            data_prepping_movies_pipeline,
            data_prepping_ratings_pipeline,
            test_and_training_split_pipeline,
            matrix_generation_pipeline,
            training_collaborative_filter_pipeline
        )
    }
