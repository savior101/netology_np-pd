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


def classificate_geo(row):
    """
    Функция принимает на вход series и классифицирует запросы пользователей по регионам запроса согласно условиям:
    geo_data = {'Центр': ['москва', 'тула', 'ярославль'],
    'Северо-Запад': ['петербург', 'псков', 'мурманск'],
    'Дальний Восток': ['владивосток', 'сахалин', 'хабаровск']}
    """
    moscow_pattern = r'\bмоскв[а-я]*\b'
    tula_pattern = r'\bтул[а-я]*\b'
    yaroslavl_pattern = r'\bярославл[а-я]*\b'
    peterburg_pattern = r'\bпетербург[а-я]*\b'
    pskov_pattern = r'\bпсков[а-я]*\b'
    murmansk_pattern = r'\bмурманск[а-я]*\b'
    vladivistok_pattern = r'\bвладивосток[а-я]*\b'
    sahalin_pattern = r'\bсахалин[а-я]*\b'
    habarovsk_pattern = r'\bхабаровск[а-я]*\b'
    if re.search(moscow_pattern, row, flags=re.I)\
            or re.search(tula_pattern, row, flags=re.I)\
            or re.search(yaroslavl_pattern, row, flags=re.I):
        return 'Центр'
    elif re.search(peterburg_pattern, row, flags=re.I)\
            or re.search(pskov_pattern, row, flags=re.I)\
            or re.search(murmansk_pattern, row, flags=re.I):
        return 'Северо-Запад'
    elif re.search(vladivistok_pattern, row, flags=re.I)\
            or re.search(sahalin_pattern, row, flags=re.I)\
            or re.search(habarovsk_pattern, row, flags=re.I):
        return 'Дальний Восток'
    else:
        return 'undefined'


@timeit
def main():
    keywords_df = pd.read_csv('keywords.csv')
    keywords_df['region'] = keywords_df['keyword'].apply(classificate_geo)
    return keywords_df


print(main())
