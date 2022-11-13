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
def power_baltic_states():
    bs_df = pd.read_csv('power.csv')
    pow = (
        bs_df[
            (bs_df['country'].isin(['Latvia', 'Lithuania', 'Estonia']))
            & (bs_df['category'].isin([4, 12, 21]))
            & (2005 <= bs_df['year'])
            & (bs_df['year'] <= 2010)
            & (bs_df['quantity'] > 0)
               ]
        ['quantity']
        .sum()
    )

    return pow


print(power_baltic_states())

# Result:
# Execution time: 0:00:02.933206
# 240580.0
