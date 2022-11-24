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


rzd = pd.DataFrame(
    {
        'client_id': [111, 112, 113, 114, 115],
        'rzd_revenue': [1093, 2810, 10283, 5774, 981]
    }
)
auto = pd.DataFrame(
    {
        'client_id': [113, 114, 115, 116, 117],
        'auto_revenue': [57483, 83, 912, 4834, 98]
    }
)
air = pd.DataFrame(
    {
        'client_id': [115, 116, 117, 118],
        'air_revenue': [81, 4, 13, 173]
    }
)
client_base = pd.DataFrame(
    {
        'client_id': [111, 112, 113, 114, 115, 116, 117, 118],
        'address': ['Комсомольская 4', 'Энтузиастов 8а', 'Левобережная 1а', 'Мира 14', 'ЗЖБИиДК 1',
                    'Строителей 18', 'Панфиловская 33', 'Мастеркова 4']
    }
)


def merge_table(rzd, auto, air, client_base):
    result_df = (
        client_base
        .merge(rzd, how='left', on='client_id')
        .merge(auto, how='left', on='client_id')
        .merge(air, how='left', on='client_id')
        .fillna(0)
    )
    return result_df


@timeit
def main(rzd, auto, air, client_base, is_drop_address=True):
    if is_drop_address:
        return merge_table(rzd, auto, air, client_base).drop('address', axis=1)
    else:
        return merge_table(rzd, auto, air, client_base)


print('Таблица без адреса:\n', main(rzd, auto, air, client_base))
print('Таблица с адресом:\n', main(rzd, auto, air, client_base, False))
