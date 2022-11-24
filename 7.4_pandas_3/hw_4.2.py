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


@timeit
def filter_news_by_url():
    """
    Функция фильтрует выбирает из файла URLs.txt новостные ссылке по паттерну: /, затем 8 цифр, затем дефис.
    """
    urls_df = pd.read_csv('URLs.txt')
    urls_df = urls_df[urls_df['url'].str.contains(r'\/\d{8}-', regex=True)]
    return urls_df


print(filter_news_by_url())
