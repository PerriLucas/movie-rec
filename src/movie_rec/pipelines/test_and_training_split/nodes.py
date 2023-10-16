"""This is a boilerplate pipeline 'feature_engineering' generated using Kedro
0.18.4."""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

#Filter out movies with no ratings, so we have 2 matrixes that can speak to one another later
def final_movie_filter() :
    final_movies = movies_titleless[movies_titleless['movieId'].isin(movies_with_ratings)]
    return final_movies

def final_movie_matrix() :
    final_movies = final_movies.set_index('movieId')
    return final_movies

#Prepare test dataset by labeling rows in different population ranges
def grouped_population() :
    def group_ratings(total_ratings):
        if total_ratings < 5 :
            return 'Menos de 5'
        if 5 <= total_ratings < 15:
            return '5 a 14'
        if 15 <= total_ratings < 30 :
            return '15 a 29'
        if 30 <= total_ratings < 50 :
            return '30 a 49'
        if 50 <= total_ratings < 100 :
            return '50 a 99'
        else:
            return 'Mais de 100'
    total_ratings_in['range'] = total_ratings_in['total_ratings'].apply(group_ratings)
    return total_ratings_in

def stratify_dataset() :
    train_df, stratified_sample = train_test_split(total_ratings_in, test_size=0.1, stratify=total_ratings_in['range'])
    return train_df, stratified_sample

def prepare_test_df() :
    test_df = stratified_sample.drop(['total_ratings', 'range'], axis=1)
    return test_df

def prepare_train_df() :
    train_df = train_df.drop(['total_ratings', 'range'], axis=1)
    return train_df
