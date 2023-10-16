from kedro.extras.datasets.pandas import CSVDataSet
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

#Filter out movies with no ratings, so we have 2 matrixes that can speak to one another later
def final_movie_filter(movies_titleless, movies_with_ratings) :
    final_movies = movies_titleless[movies_titleless['movieId'].isin(movies_with_ratings)]
    return final_movies

def final_movie_matrix(final_movies) :
    final_movies_fixed = final_movies.set_index('movieId')
    return final_movies_fixed

#Prepare test dataset by labeling rows in different population ranges
def grouped_population(total_ratings_in) :
    grouped_ratings = total_ratings_in
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
    grouped_ratings['range'] = grouped_ratings['total_ratings'].apply(group_ratings)
    return grouped_ratings

def stratify_dataset(grouped_ratings) :
    training_sample, stratified_sample = train_test_split(grouped_ratings, test_size=0.1, stratify=grouped_ratings['range'])
    return training_sample, stratified_sample

def prepare_test_df(stratified_sample) :
    test_df = stratified_sample.drop(['total_ratings', 'range'], axis=1)
    return test_df

def prepare_train_df(training_sample) :
    train_df = training_sample.drop(['total_ratings', 'range'], axis=1)
    train_df_df = pd.DataFrame(train_df)
    return train_df, train_df_df
