"""This is a boilerplate pipeline 'feature_engineering' generated using Kedro
0.18.4."""

import pandas as pd
import numpy as np

def ratings_raw_data_get() :
    ratings = pd.read_csv('/data/01_raw/ratings.csv', header=0, index_col = 0)
    return ratings

#remove timestamp rating column
def drop_timestamp() :
    ratings = ratings.drop('timestamp', axis=1)
    return ratings

# Filter out movies without genres
def filter_out_movies_no_genre() :
    ratings = ratings[ratings['movieId'].isin(movie_with_genres)]
    return ratings

#Create a list of movies with ratings
def movies_with_ratings() :
    movies_with_ratings = ratings['movieId'].unique()
    return movies_with_ratings

# Genereate a matrix of user ID x Movie where the intersections are the ratings given to the movies
def pivot_ratings() :
    pivoted_ratings = ratings.pivot_table(index= 'userId', columns='movieId', values='rating', fill_value= 0 , aggfunc='mean', )
    return pivoted_ratings

 #Remove every movie with only 2 or less ratings
def remove_outliers() :
    movie_ratings_count = pivoted_ratings.count()
    filtered_movies = movie_ratings_count[movie_ratings_count >= 3]
    filtered_pivoted_ratings = pivoted_ratings[filtered_movies.index]
    return filtered_pivoted_ratings

def create_total_ratings() :
    filtered_pivoted_ratings['total_ratings'] = filtered_pivoted_ratings.count()
    return pivoted_ratings

#Remove Users with no ratings
def ratingless_users() :
    final_ratings = pivoted_ratings[pivoted_ratings['total_ratings'] > 0] 
    total_ratings_in = final_ratings
    return total_ratings_in

#remove rating column for the matrix use
def final_ratings() :
    final_ratings = final_ratings.drop('total_ratings', axis=1)
    return final_ratings