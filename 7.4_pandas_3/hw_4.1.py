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


def sort_by_traffic_source(df):
    """
    Функция принимает на вход строку df и возвращает значение столбца source_type по правилам:
        * если источник traffic_source равен Yandex или Google, то в source_type ставится organic;
        * для источников paid и email из России ставим ad;
        * для источников paid и email не из России ставим other;
        * все остальные варианты берём из traffic_source без изменений.
    """
    if df['traffic_source'] in ('yandex', 'google'):
        return 'organic'
    elif df['traffic_source'] in ('paid', 'email') and df['region'] == 'Russia':
        return 'ad'
    elif df['traffic_source'] in ('paid', 'email') and df['region'] != 'Russia':
        return 'other'
    else:
        return df['traffic_source']


@timeit
def visit_log():
    visit_log_df = pd.read_csv('visit_log.csv', sep=';')
    visit_log_df['source_type'] = visit_log_df.apply(sort_by_traffic_source, axis=1)
    return visit_log_df


print(visit_log())
