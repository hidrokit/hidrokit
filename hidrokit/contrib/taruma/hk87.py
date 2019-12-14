"""manual: SNI 6738:2015
https://gist.github.com/taruma/0b0ebf3ba12d4acf7cf11df905d2ec9c
"""


import numpy as np
import pandas as pd


def prob_weibull(m, n):
    return m / (n + 1) * 100


def _array_weibull(n):
    return np.array([prob_weibull(i, n) for i in range(1, n + 1)])


def _fdc_xy(df):
    n = len(df.index)
    x = _array_weibull(n)
    y = df.sort_values(ascending=False).values
    return x, y


def _interpolate(probability, x, y):
    return {p: np.interp(p, x, y) for p in probability}


def debit_andal(df, column, kind='table', prob=[80, 90, 95]):
    x, y = _fdc_xy(df.loc[:, column])

    if kind.lower() == 'array':
        return x, y

    if kind.lower() == 'prob':
        return _interpolate(prob, x, y)

    if kind.lower() == 'table':
        data = {
            'idx': df.loc[:, column].sort_values(ascending=False).index,
            'rank': list(range(1, len(df.index) + 1)),
            'prob': x,
            'data': y,
        }
        return pd.DataFrame(data)


def debit_andal_bulanan(df, column, **kwargs):
    return {
        m: debit_andal(df[df.index.month == m], column, **kwargs)
        for m in range(1, 13)
    }
