import pandas as pd
from datetime import datetime
import re


def timeit(function):
    """
    Декоратор для подсчета времени работы функций
    """
    def wrapped(*args):
        start_time = datetime.now()
        result = function(*args)
        print(f'Execution time: {datetime.now() - start_time}')
        return result

    return wrapped


def production_year(row):
    """
    Функция получает на вход строки series, выбирает год выпуска фильма и, если он находится
    в промежутке между 1950 и 2010 включительно, то возвращает соответствующий год. Если год в названии отсутствует или
    выходит за рамки периода 1950-2010, то возвращается 1900 год.
    """
    years = [x for x in range(1950, 2011)]
    year_pattern = r'(\()(\d\d\d\d)(\))'
    if re.search(year_pattern, row):
        movie_year = int(re.search(year_pattern, row).group(2))
        if movie_year in years:
            return movie_year
        else:
            return 1900
    else:
        return 1900


@timeit
def main():
    ratings_df = pd.read_csv('ratings.csv')
    movies_df = pd.read_csv('movies.csv')
    movies_df['year'] = movies_df['title'].apply(production_year)
    movies_df = (
        movies_df
        .merge(ratings_df, how='left', on='movieId')
        .groupby('year')
        .agg({'rating': 'mean'})
        .sort_values(by='rating', ascending=False)
        .reset_index()
    )
    return movies_df


print(main())
