import pandas as pd
from datetime import datetime

# отобразить все столбцы
pd.set_option('max_columns', None)


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


@timeit
def ttl():
    """
    Функция выбирает id пользователей, которые поставили больше 100 оценок и считает их время жизни на сайте.
    Под временем жизни понимается разница между максимальным и минимальным значениями столбца
    timestamp для данного значения userId.
    """
    rating_df = pd.read_csv('ratings.csv')
    rating_df = rating_df.groupby('userId').agg({'movieId': 'count', 'timestamp': ['min', 'max']})
    rating_df = rating_df[rating_df['movieId']['count'] > 100]
    rating_df['min'] = pd.to_datetime(rating_df['timestamp']['min'], unit='s')
    rating_df['max'] = pd.to_datetime(rating_df['timestamp']['max'], unit='s')
    rating_df['user_ttl'] = rating_df.apply(lambda x: x['max'] - x['min'], axis=1)
    res_df = rating_df.drop(['timestamp', 'movieId', 'min', 'max'], axis=1).reset_index()
    return res_df


print(ttl())
