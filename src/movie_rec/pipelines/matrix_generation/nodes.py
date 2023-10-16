"""This is a boilerplate pipeline 'serving' generated using Kedro 0.18.4."""

import pandas as pd
import numpy as np
from scipy.sparse import csr_matrix

def generate_training_ratings(train_df) :
    rec_matrix = csr_matrix(train_df)
    return rec_matrix

def generate_feature_matrix(final_movies_fixed) :
    final_movies_matrix = csr_matrix(final_movies_fixed)
    return final_movies_matrix

def transfom_genre_list(unique_genres) :
    unique_genres_list = list(unique_genres)
    return unique_genres_list

def generate_empty_matrix(unique_genres_list,rec_matrix) :
    len_rec_matrix = rec_matrix.shape[0]
    len_features = len(unique_genres_list)-1
    user_feature_empty = csr_matrix((len_rec_matrix, len_features), dtype=np.float64)
    return user_feature_empty

def aux_matrix(rec_matrix,final_movies_matrix) :
    aux_matrix_train = np.dot(rec_matrix, final_movies_matrix)
    return aux_matrix_train

def test_matrix(test_df) :
    test_matrix = csr_matrix(test_df)
    return test_matrix