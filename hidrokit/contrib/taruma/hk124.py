"""
hk124: freq_lognormal.py

This module provides functions for calculating values related to hydrological analysis.

For more information, refer to the manual: 
    https://gist.github.com/taruma/5d3ab88893e56f895dc3f36ea19c3e60

Functions:
- find_K: Calculates the K value for a given return period.
- calc_x_lognormal: Calculates the x value for a given return period 
    using the lognormal distribution.
- freq_lognormal: Calculates the lognormal frequency distribution for a given dataset.
- calc_prob: Calculates the probability for a given K value.
"""

import numpy as np
import pandas as pd
from scipy import stats
from hidrokit.contrib.taruma.utils import handle_deprecated_params

# pylint: disable=invalid-name

# Tabel Nilai Variabel Reduksi Gauss
# Dari buku hidrologi: Aplikasi Metode Statistik untuk Analisa Data. hal.119

# KODE: SW (Source: Soewarno)

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

_COL_SW = ["periode_ulang", "peluang", "k"]

t_normal_sw = pd.DataFrame(data=_DATA_SW, columns=_COL_SW)


def _find_k_in_table(return_period, table):
    x = table.periode_ulang
    y = table.k
    return np.interp(return_period, x, y)


def find_K(return_period, source="scipy"):
    """
    Calculate the K values for a given return period.

    Parameters:
        return_period (float or array-like): The return period(s) for
            which to calculate the K values.
        source (str, optional): The source of the K values.
            Can be "soewarno" or "scipy". Defaults to "scipy".

    Returns:
        array-like: The calculated K values.

    Raises:
        ValueError: If an unknown source is provided.

    """
    if source.lower() == "soewarno":
        k_values = _find_k_in_table(return_period, t_normal_sw)
    elif source.lower() == "scipy":
        return_period = np.array(return_period)
        k_values = stats.norm.ppf(1 - 1 / return_period)
    else:
        raise ValueError(f"Unknown source: {source}")
    return k_values


def calc_x_lognormal(x, return_period=None, source="scipy", show_stat=False):
    """
    Calculate the value of x for a given return period using the lognormal distribution.

    Parameters:
        x (array-like): Input data array.
        return_period (array-like, optional):
            Return period(s) for which to calculate the value of x.
            Default is [5].
        source (str, optional): Source of the K factor.
            Default is "scipy".
        show_stat (bool, optional): Whether to display the calculated statistics.
            Default is False.

    Returns:
        array-like: The calculated value(s) of x for the given return period(s).
    """
    return_period = [5] if return_period is None else return_period
    return_period = np.array(return_period)
    y = np.log10(x)
    y_mean = np.mean(y)
    y_std = np.std(y, ddof=1)

    k = find_K(return_period, source=source)

    if show_stat:
        print(f"y_mean = {y_mean:.5f}")
        print(f"y_std = {y_std:.5f}")
        print(f"k = {k}")

    val_y = y_mean + k * y_std
    val_x = np.power(10, val_y)
    return val_x


def freq_lognormal(
    dataframe=None,
    target_column=None,
    return_periods=None,
    display_stat=False,
    source="scipy",
    out_column_name="Log Normal",
    out_index_name="Kala Ulang",
    **kwargs,
):
    """
    Calculate the frequency analysis using the lognormal distribution.

    Parameters:
    - dataframe (pandas.DataFrame): The input dataframe containing the data.
    - target_column (str):
        The name of the column in the dataframe that contains the data to be analyzed.
    - return_periods (list): A list of return periods for which the analysis will be performed.
        Default is [2, 5, 10, 20, 25, 50, 100].
    - display_stat (bool): Whether to display the statistical information. Default is False.
    - source (str): The source of the lognormal distribution. Default is "scipy".
    - out_column_name (str): The name of the output column in the result dataframe.
        Default is "Log Normal".
    - out_index_name (str): The name of the index column in the result dataframe.
        Default is "Kala Ulang".
    - **kwargs: Additional keyword arguments for deprecated parameters.

    Returns:
    - result (pandas.DataFrame): The result dataframe containing the frequency analysis results.

    """
    # deprecated parameters
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

    arr = calc_x_lognormal(
        x, return_period=return_periods, show_stat=display_stat, source=source
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
    Calculate the probability value for a given value of k.

    Parameters:
    - k (float or array-like): The value(s) for which the probability is calculated.
    - source (str, optional): The source of probability calculation.
                              Valid options are "soewarno" and "scipy".
                              Default is "scipy".

    Returns:
    - prob_value (float or array-like): The calculated probability value(s).

    Raises:
    - ValueError: If an unknown source is provided.

    """
    if source.lower() == "soewarno":
        k = np.array(k)
        prob_value = 1 - _calc_prob_in_table(k, t_normal_sw)
    elif source.lower() == "scipy":
        prob_value = stats.norm.cdf(k)
    else:
        raise ValueError(f"Unknown source: {source}")
    return prob_value
