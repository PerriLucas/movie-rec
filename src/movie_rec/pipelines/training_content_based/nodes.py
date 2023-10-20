"""This is a boilerplate pipeline 'training' generated using Kedro 0.18.4."""

import pandas as pd
import numpy as np
from scipy.sparse import csr_matrix
from sklearn.metrics.pairwise import cosine_similarity

# Normalizing the matrix
def user_feature_matrix(user_feature_empty,len_rec_matrix, rec_matrix,aux_matrix_train) :
    user_feature = user_feature_empty
    for u in range(len_rec_matrix):
        n_notnull = rec_matrix[u,:].count_nonzero()
        user_feature[u,:] = np.dot(1/float(n_notnull), aux_matrix_train[u,:])
    user_feature_df = pd.DataFrame(user_feature)
    return user_feature, user_feature_df

def cosine_similarity_prediction(user_feature,final_movies_matrix) :
    prediction = cosine_similarity(user_feature,final_movies_matrix)
    prediction_df = pd.DataFrame(prediction)
    return prediction,prediction_df 

def rec_size() :
    rec_size = 5
    return rec_size

def user_recommendation(test_matrix,rec_size,prediction) :
    recommendation = {}

    for u in range(test_matrix.shape[0]) :
      recommendation[u] = []
      cont = 0
      order = np.argsort(prediction[u,:])[::-1]
      for i in order :
        if (cont < rec_size) :
            if (test_matrix[u,i] == float(0)) :
              recommendation[u].append(i)
            cont += 1
        else:
          break
    
    return recommendation

# Expand the lists of movie IDs into separate rows
def expand_cb_rec_list(recommendation) :
    max_length_cb = max(len(ids) for ids in recommendation.values())
    return max_length_cb

# Pad the lists with None to make them all the same length
def list_padding_cb(recommendation, max_length_cb) :
    for key in recommendation:
        recommendation[key] = recommendation[key] + [None] * (max_length_cb - len(recommendation[key]))
    recommendation_padded = recommendation
    return recommendation_padded

# Convert the dictionary to a DataFrame
def convert_cb_df(recommendation_padded) :
    recommendations_df = pd.DataFrame.from_dict(recommendation_padded, orient='index')
    recommendations_df.columns = ['first_rec', 'second_rec', 'third_rec', 'fourth_rec', 'fifth_rec']
    return recommendations_df

def fixed_cb_recs(recommendations_df, movies) :
    movie_title = movies[['title', 'movieId']]
    user_movies_df = recommendations_df.merge(movie_title, left_on='first_rec', right_index=True, how='left')
    user_movies_df = user_movies_df.merge(movie_title, left_on='second_rec', right_index=True, how='left', suffixes=('', '2'))
    user_movies_df = user_movies_df.merge(movie_title, left_on='third_rec', right_index=True, how='left', suffixes=('', '3'))
    user_movies_df = user_movies_df.merge(movie_title, left_on='fourth_rec', right_index=True, how='left', suffixes=('', '4'))
    user_movies_df = user_movies_df.merge(movie_title, left_on='fifth_rec', right_index=True, how='left', suffixes=('', '5'))
    drop_columns = ['first_rec', 'second_rec',	'third_rec'	,'fourth_rec',	'fifth_rec', 'movieId', 'movieId2', 'movieId3', 'movieId4', 'movieId5',]
    user_movies_df = user_movies_df.drop(columns=drop_columns)
    user_movies_df.columns = ['first_rec', 'second_rec', 'third_rec', 'fourth_rec', 'fifth_rec']
    rec_cb = user_movies_df
    return rec_cb

#save output in a csv
def output_cb(rec_cb) :
    rec_cb_output = pd.DataFrame(rec_cb)
    return rec_cb_output