"""
hk172: freq_normal.py
======================

This module provides functions for calculating the 
    K value, normal value, and frequency of the normal distribution.

Functions:
- find_K: Find the K value for a given set of return periods.
- calc_x_normal: Calculate the normal value using the mean and 
    standard deviation of an input array.
- freq_normal: Calculate the frequency of the normal distribution for a given dataset.
- calc_prob: Calculate the probability of a value being less than or equal to k.

For more information, refer to the manual: 
    https://gist.github.com/taruma/91b9fcd8fb92c12f4ea2639320ead116
"""

import numpy as np
import pandas as pd
from scipy import stats
from hidrokit.contrib.taruma.utils import handle_deprecated_params

# fmt: off

# Tabel Nilai Variabel Reduksi Gauss
# Dari buku hidrologi: Aplikasi Metode Statistik untuk Analisa Data. hal.119

# KODE: SW

_DATA_SW = [
    [1.001, 0.999, -3.050],
    [1.005, 0.995, -2.580],
    [1.010, 0.990, -2.330],
    [1.050, 0.950, -1.640],
    [1.110, 0.900, -1.280],
    [1.250, 0.800, -0.840],
    [1.330, 0.750, -0.670],
    [1.430, 0.700, -0.520],
    [1.670, 0.600, -0.250],
    [2.000, 0.500, 0.000],
    [2.500, 0.400, 0.250],
    [3.330, 0.300, 0.520],
    [4.000, 0.250, 0.670],
    [5.000, 0.200, 0.840],
    [10.000, 0.100, 1.280],
    [20.000, 0.050, 1.640],
    [50.000, 0.200, 2.050],
    [100.000, 0.010, 2.330],
    [200.000, 0.005, 2.580],
    [500.000, 0.002, 2.880],
    [1000.000, 0.001, 3.090],
]

_COL_SW = ['periode_ulang', 'peluang', 'k']

t_normal_sw = pd.DataFrame(
    data=_DATA_SW, columns=_COL_SW
)

# fmt: on


def _find_k_in_table(return_period, table):
    x = table.periode_ulang
    y = table.k
    return np.interp(return_period, x, y)


def find_K(
    return_periods=None, source="scipy", **kwargs
):  # pylint: disable=invalid-name
    """
    Find the K value for a given set of return periods.

    Parameters:
        return_periods (list or array-like): List of return periods.
        source (str): Source for calculating K value. Options are 'soewarno' or 'scipy'.
        **kwargs: Additional keyword arguments.

    Returns:
        numpy.ndarray: Array of K values corresponding to the given return periods.

    Raises:
        ValueError: If the source is not 'soewarno' or 'scipy'.
    """
    # handle deprecated params
    return_periods = (
        handle_deprecated_params(kwargs, "return_period", "return_periods")
        or return_periods
    )

    if source.lower() == "soewarno":
        return _find_k_in_table(return_periods, t_normal_sw)
    if source.lower() == "scipy":
        return_periods = np.array(return_periods)
        return stats.norm.ppf(1 - 1 / return_periods)
    raise ValueError("source must be 'soewarno' or 'scipy'.")


def calc_x_normal(
    input_array=None, return_periods=None, source="scipy", display_stat=False, **kwargs
):
    """
    Calculate the normal value (val_x) using the mean and standard deviation of an input array.

    Parameters:
    - input_array (array-like): The input array of values.
    - return_periods (array-like, optional):
        The return periods for which to calculate the normal value. Default is [5].
    - source (str, optional): The source of the return period values. Default is "scipy".
    - display_stat (bool, optional): Whether to display the calculated statistics.
        Default is False.
    - **kwargs: Additional keyword arguments for handling deprecated parameters.

    Returns:
    - val_x (float or array-like): The calculated normal value(s) based on the input array.

    """

    # handle deprecated params
    input_array = handle_deprecated_params(kwargs, "x", "input_array") or input_array
    return_periods = (
        handle_deprecated_params(kwargs, "return_period", "return_periods")
        or return_periods
    )
    display_stat = (
        handle_deprecated_params(kwargs, "show_stat", "display_stat") or display_stat
    )

    return_periods = [5] if return_periods is None else return_periods

    return_periods = np.array(return_periods)
    input_array = np.array(input_array)
    data_mean = np.mean(input_array)
    data_std = np.std(input_array, ddof=1)
    data_count = input_array.size

    k = find_K(return_periods, source=source)

    if display_stat:
        print(f"x_mean = {data_mean:.5f}")
        print(f"x_std = {data_std:.5f}")
        print(f"k = {k}")
        print(f"n = {data_count}")

    x_values = data_mean + k * data_std
    return x_values


def freq_normal(
    dataframe=None,
    target_column=None,
    return_periods=None,
    display_stat=False,
    source="scipy",
    out_column_name="Normal",
    out_index_name="Kala Ulang",
    **kwargs,
):
    """
    Calculate the frequency of normal distribution for a given dataset.

    Args:
        dataframe (pd.DataFrame): The input dataframe containing the data.
        target_column (str): The name of the column in the dataframe to be used
            as the target variable.
        return_periods (list): A list of return periods to calculate the frequency for.
            If None, default return periods [2, 5, 10, 20, 25, 50, 100] will be used.
        display_stat (bool): Whether to display the statistical
            summary of the normal distribution.
            Default is False.
        source (str): The source of the normal distribution calculation.
            Default is "scipy".
        out_column_name (str): The name of the output column in the result dataframe.
            Default is "Normal".
        out_index_name (str): The name of the index in the result dataframe.
            Default is "Kala Ulang".
        **kwargs: Additional keyword arguments for deprecated parameters.

    Returns:
        pd.DataFrame: A dataframe containing the frequency of the normal distribution
            for the specified return periods.

    Deprecated Parameters:
        - df (pd.DataFrame): Use `dataframe` instead.
        - col (str): Use `target_column` instead.
        - return_period (list): Use `return_periods` instead.
        - show_stat (bool): Use `display_stat` instead.
        - col_name (str): Use `out_column_name` instead.
        - index_name (str): Use `out_index_name` instead.
    """

    # handle deprecated params
    dataframe = handle_deprecated_params(kwargs, "df", "dataframe") or dataframe
    target_column = (
        handle_deprecated_params(kwargs, "col", "target_column") or target_column
    )
    return_periods = (
        handle_deprecated_params(kwargs, "return_period", "return_periods")
        or return_periods
    )
    display_stat = (
        handle_deprecated_params(kwargs, "show_stat", "display_stat") or display_stat
    )
    out_column_name = (
        handle_deprecated_params(kwargs, "col_name", "out_column_name")
        or out_column_name
    )
    out_index_name = (
        handle_deprecated_params(kwargs, "index_name", "out_index_name")
        or out_index_name
    )

    return_periods = (
        [2, 5, 10, 20, 25, 50, 100] if return_periods is None else return_periods
    )

    target_column = dataframe.columns[0] if target_column is None else target_column

    x = dataframe[target_column].copy()

    arr = calc_x_normal(
        x, return_periods=return_periods, display_stat=display_stat, source=source
    )

    result = pd.DataFrame(data=arr, index=return_periods, columns=[out_column_name])

    result.index.name = out_index_name
    return result


def _calc_prob_in_table(k, table):
    x = table.k
    y = table.peluang
    return np.interp(k, x, y)


def calc_prob(k, source="scipy"):
    """
    Calculate the probability of a value being less than or equal to k.

    Parameters:
    - k (float or array-like): The value(s) to calculate the probability for.
    - source (str, optional): The source to use for probability calculation.
                              Valid options are 'soewarno' or 'scipy'.
                              Defaults to 'scipy'.

    Returns:
    - prob (float or array-like): The calculated probability value(s).

    Raises:
    - ValueError: If the source is not 'soewarno' or 'scipy'.

    """
    if source.lower() == "soewarno":
        k = np.array(k)
        return 1 - _calc_prob_in_table(k, t_normal_sw)
    if source.lower() == "scipy":
        return stats.norm.cdf(k)
    raise ValueError("source must be 'soewarno' or 'scipy'.")
