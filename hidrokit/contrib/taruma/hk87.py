"""manual: SNI 6738:2015
https://gist.github.com/taruma/0b0ebf3ba12d4acf7cf11df905d2ec9c
"""


import numpy as np
import pandas as pd
from hidrokit.contrib.taruma.utils import deprecated

def calculate_weibull_probability(shape, scale):
    """
    Calculate the Weibull probability.

    Parameters:
        shape (float): The shape parameter of the Weibull distribution.
        scale (float): The scale parameter of the Weibull distribution.

    Returns:
        float: The calculated Weibull probability.
    """
    return shape / (scale + 1) * 100


def _array_weibull(n):
    return np.array([calculate_weibull_probability(i, n) for i in range(1, n + 1)])


def _fdc_xy(df):
    n = len(df.index)
    x = _array_weibull(n)
    y = df.sort_values(ascending=False).values
    return x, y


def _interpolate(probability, x, y):
    return {p: np.interp(p, x, y) for p in probability}


def dependable_flow(dataframe, column_name, return_type=None, probabilities=None):
    """
    Calculate the dependable flow values based on a given dataframe and column name.

    Parameters:
        dataframe (pd.DataFrame): The input dataframe.
        column_name (str): The name of the column in the dataframe.
        return_type (str, optional): The type of the return value. Default is None ('table').
            Possible values are 'array', 'prob', and 'table'.
        probabilities (list, optional): The list of probabilities to calculate. Default is None.
            Only applicable when return_type is 'prob'.

    Returns:
        If return_type is 'array', returns a tuple of x_values and y_values.
        If return_type is 'prob', returns the interpolated values based on the given probabilities.
        If return_type is None / 'table', returns a pandas DataFrame with the following columns:
            - index: The index of the dataframe sorted in descending order.
            - rank: The rank of each value in the dataframe.
            - probability: The x-values.
            - data: The y-values.
    """
    probabilities = [80, 90, 95] if probabilities is None else probabilities
    x_values, y_values = _fdc_xy(dataframe.loc[:, column_name])

    if return_type.lower() == 'array':
        return x_values, y_values

    if return_type.lower() == 'prob':
        return _interpolate(probabilities, x_values, y_values)

    data = {
        'index': dataframe.loc[:, column_name].sort_values(ascending=False).index,
        'rank': list(range(1, len(dataframe.index) + 1)),
        'probability': x_values,
        'data': y_values,
    }
    return pd.DataFrame(data)


@deprecated("dependable_flow")
def debit_andal(df, column, kind='table', prob=None):
    """Calculate dependable flow based on SNI 6738:2015"""
    return dependable_flow(df, column, kind, prob)


def debit_andal_bulanan(df, column, **kwargs):
    return {
        m: dependable_flow(df[df.index.month == m], column, **kwargs)
        for m in range(1, 13)
    }
