"""This is a boilerplate pipeline 'training' generated using Kedro 0.18.4."""

import pandas as pd
import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse import linalg

def factors() :
    factors = 19
    return factors

# Get the matrixes for the SVD method
def svd_matrixes() :
    [user_vector, eingenvalues, movie_vector] = linalg.svds(rec_matrix, factors, return_singular_vectors=True)
    return user_vector, eingenvalues, movie_vector

# Generate user x item matrix
def user_item_matrix() :
    len_users = rec_matrix.shape[0]
    len_movies = rec_matrix.shape[1]
    user_movies = csr_matrix((len_users, len_movies), dtype=np.float64)
    return user_movies

def transpose_item_matrix() :
    movie_vector_t = movie_vector.transpose()
    return movie_vector_t

def aux_matrix_train_cf() :
    aux_matrix = rec_matrix.dot(movie_vector_t)
    return aux_matrix

# Apply approximate SVD model to obtain approximate relevance vectors
def user_movies_vectors() :
    aux_matrix = rec_matrix.dot(movie_vector_t)
    user_movies = aux_matrix.dot(movie_vector)
    return user_movies

def rec_size() :
    rec_size = 5
    return rec_size

def prediction_cf() :
    recommended_cf = {}

    for u in range(test_matrix.shape[0]) :
        recommended_cf[u] = []
        cont = 0
        order = np.argsort(user_movies[u,:])[::-1]
        for i in order :
            if (cont < rec_size) :
                if (test_matrix[u,i] == float(0)) :
                    recommended_cf[u].append(i)
                    cont += 1
            else:
                break
    return recommended_cf

# Expand the lists of movie IDs into separate rows
def expand_cf_rec_list() :
    max_length = max(len(ids) for ids in recommended_cf.values())
    return max_length

# Pad the lists with None to make them all the same length
def list_padding_cf() :
    for key in recommended_cf:
        recommended_cf[key] = recommended_cf[key] + [None] * (max_length - len(recommended_cf[key]))
    return recommended_cf

def convert_cf_df() :
    recommended_cf = pd.DataFrame.from_dict(recommended_cf, orient='index')
    recommended_cf.columns = ['first_rec', 'second_rec', 'third_rec', 'fourth_rec', 'fifth_rec']
    return recommended_cf

# Merge with movie_info_df to get movie titles, clean the dataset
def fixed_cf_recs() :
    movie_title = movies[['title', 'movieId']]
    rec_cf = recommended_cf.merge(movie_title, left_on='first_rec', right_index=True, how='left')
    rec_cf = rec_cf.merge(movie_title, left_on='second_rec', right_index=True, how='left', suffixes=('', '2'))
    rec_cf = rec_cf.merge(movie_title, left_on='third_rec', right_index=True, how='left', suffixes=('', '3'))
    rec_cf = rec_cf.merge(movie_title, left_on='fourth_rec', right_index=True, how='left', suffixes=('', '4'))
    rec_cf = rec_cf.merge(movie_title, left_on='fifth_rec', right_index=True, how='left', suffixes=('', '5'))
    drop_columns = ['first_rec', 'second_rec',	'third_rec'	,'fourth_rec',	'fifth_rec', 'movieId', 'movieId2', 'movieId3', 'movieId4', 'movieId5',]
    rec_cf = rec_cf.drop(columns=drop_columns)
    rec_cf.columns = ['first_rec', 'second_rec', 'third_rec', 'fourth_rec', 'fifth_rec']
    return rec_cf
        
#save output in a csv
def output_cf() :
    rec_cf.to_csv('rec_cf_model.csv', index=False)
    return rec_cf