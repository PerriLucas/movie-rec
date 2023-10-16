"""Project pipelines."""
from typing import Dict

from kedro.pipeline import Pipeline

from movie_rec.pipelines import feature_engineering as fe
from movie_rec.pipelines import serving, training

# from kedro.framework.project import find_pipelines


def register_pipelines() -> Dict[str, Pipeline]:
    """Register the project's pipelines.

    Returns:
        A mapping from pipeline names to ``Pipeline`` objects.
    """
    feature_engineering_pipeline = fe.create_pipeline()
    training_pipeline = training.create_pipeline()
    serving_pipeline = serving.create_pipeline()

    # Leaving this commented as it is a new feature and could be useful eventually
    # As of today, I'm against running everything by default.
    # pipelines = find_pipelines()
    # pipelines["__default__"] = sum(pipelines.values())

    return {
        "feature_engineer": feature_engineering_pipeline,
        "train": training_pipeline,
        "serve": serving_pipeline,
        "train_and_generate_metrics": (
            feature_engineering_pipeline + training_pipeline + serving_pipeline
        ),
    }
