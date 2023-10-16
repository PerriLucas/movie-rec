"""This is a boilerplate pipeline 'feature_engineering' generated using Kedro
0.18.4."""

import pandas as pd
import numpy as np

def movie_raw_data_get() :
    movies = pd.read_csv('/data/01_raw/movies.csv', header=0, converters={'genres': lambda x: x[0:].split('|')})
    return movies

# Turns the unique values for the np array Genres into columns filled with 0 if the movie isnt associated with that genre, or 1 if it is
def list_unique_genres() :
    unique_genres = set(genre for genres_list in movies['genres'] for genre in genres_list)
    return unique_genres

def turn_values_into_columns() :
    for genre in unique_genres:
        movies[genre] = 0
    for index, row in movies.iterrows() :
        for genre in row['genres']:
            movies.at[index, genre] = 1
    return movies

def fix_columns_movies() :
    movies = movies.drop('genres', axis=1)
    movies.columns = movies.columns.str.replace('(', '')
    movies.columns = movies.columns.str.replace(')', '')
    movies.columns = movies.columns.str.replace(' ', '')
    return movies

#Removes movies without associated genres
def filter_out_non_genre() :
    movies = movies[movies.nogenreslisted != 1]
    return movies

def remove_non_genre_column() :
# Removes the column no genres listed
    movies = movies.drop('nogenreslisted', axis=1)
    return movies

def titleless_movies():
    #Creates a dataframe without title for use later
    movies_titleless = movies.drop('title', axis=1)
    return movies_titleless

def list_movies_with_genre() :
    #Creates a list of movie_ids that have genres
    movie_with_genres = movies['movieId'].to_list()
    return movie_with_genres
