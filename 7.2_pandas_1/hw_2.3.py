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
def stocks_from_fortrader():
    stocks = pd.read_html('https://fortrader.org/quotes')
    return stocks[3]


print(stocks_from_fortrader())
