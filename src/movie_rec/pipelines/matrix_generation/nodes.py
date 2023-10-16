"""This is a boilerplate pipeline 'serving' generated using Kedro 0.18.4."""

import pandas as pd
import numpy as np
from scipy.sparse import csr_matrix

def generate_training_ratings() :
    rec_matrix = csr_matrix(train_df)
    return rec_matrix

def generate_feature_matrix() :
    final_movies_matrix = csr_matrix(final_movies)
    return final_movies_matrix

def transfom_genre_list() :
    unique_genres = list(unique_genres)
    return unique_genres

def generate_empty_matrix() :
    len_rec_matrix = rec_matrix.shape[0]
    len_features = len(unique_genres)-1
    user_feature = csr_matrix((len_rec_matrix, len_features), dtype=np.float64)

def aux_matrix() :
    aux_matrix_train = np.dot(rec_matrix, final_movies_matrix)
    return aux_matrix_train

def test_matrix() :
    test_matrix = csr_matrix(test_df)
    return test_matrix