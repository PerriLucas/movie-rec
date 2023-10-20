from kedro.extras.datasets.pandas import CSVDataSet
import pandas as pd
import numpy as np
from scipy.sparse import csr_matrix

def generate_training_ratings(training_sample) :
    rec_matrix = csr_matrix(training_sample)
    rec_matrix_txt = pd.DataFrame.sparse.from_spmatrix(rec_matrix)
    return rec_matrix, rec_matrix_txt

def generate_feature_matrix(final_movies) :
    final_movies_matrix = csr_matrix(final_movies)
    final_movies_matrix_df = pd.DataFrame(final_movies)
    return final_movies_matrix, final_movies_matrix_df

def transfom_genre_list(unique_genres) :
    unique_genres_list = list(unique_genres)
    return unique_genres_list

def generate_empty_matrix(unique_genres_list,rec_matrix) :
    len_rec_matrix = rec_matrix.shape[0]
    len_features = len(unique_genres_list)-1
    user_feature_empty = csr_matrix(np.zeros((len_rec_matrix, len_features), dtype=np.float64))
    user_feature_empty_df = pd.DataFrame(user_feature_empty)
    return user_feature_empty, user_feature_empty_df, len_rec_matrix

def aux_matrix(rec_matrix,final_movies_matrix) :
    aux_matrix_train = np.dot(rec_matrix, final_movies_matrix)
    aux_matrix_train_df = pd.DataFrame.sparse.from_spmatrix(aux_matrix_train)
    return aux_matrix_train, aux_matrix_train_df

def test_matrix(test_df) :
    test_matrix = csr_matrix(test_df)
    return test_matrix