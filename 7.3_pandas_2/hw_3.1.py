import pandas as pd
from datetime import datetime


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


def classificate_ratings(row):
    """
    Функция принимает на вход строки series и классифицирует фильмы по рейтингам из условий:
    1. оценка 2 и ниже — низкий рейтинг;
    2. оценка 4 и ниже — средний рейтинг;
    3. оценка 4.5 и 5 — высокий рейтинг.
    P.S.: последнее тождественно от 4 до 5 включительно
    """
    if row <= 2.0:
        return 'Низкий'
    elif 2.0 < row <= 4.0:
        return 'Средний'
    elif 4.0 < row <= 5.0:
        return 'Высокий'


@timeit
def ratings():
    ratings_df = pd.read_csv('ratings.csv')
    ratings_df['class'] = ratings_df['rating'].apply(classificate_ratings)
    return ratings_df


print(ratings())
    