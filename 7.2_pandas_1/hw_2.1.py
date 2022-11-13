import pandas as pd
from datetime import datetime


def timeit(function):
    def wrapped(*args):
        start_time = datetime.now()
        result = function(*args)
        print(f'Execution time: {datetime.now() - start_time}')
        return result
    return wrapped


@timeit
def best_of_the_best_movie():
    movies_df = pd.read_csv('movies.csv')
    ratings_df = pd.read_csv('ratings.csv')
    ratings_df = ratings_df[ratings_df['rating'] == 5.0]

    max_count = (
        ratings_df['movieId']
        .value_counts(ascending=True)
        .tail(n=1)
        .to_dict()
    )
    return movies_df[movies_df['movieId'] == list(max_count.keys())[0]]


print(best_of_the_best_movie())

# Result:
# Execution time: 0:01:07.819920
#      movieId                             title       genres
# 315      318  Shawshank Redemption, The (1994)  Crime|Drama
