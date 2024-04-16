"""
hk151: outlier_hydrology.py

This module contains functions for performing outlier analysis and calculations based 
    on the Ven Te Chow method.

Functions:
- find_Kn: Find the value of Kn (Kurva N) based on the given data count.
- calc_boundary: Calculate the boundary values for a given target column in a dataframe.
- find_outlier: Find outliers in a dataframe based on a target column.

manual:
    https://gist.github.com/taruma/7bf2e4e1601ab8390d9919043eb87682
"""

import numpy as np
import pandas as pd
from hidrokit.contrib.taruma.utils import handle_deprecated_params

# pylint: disable=invalid-name
# fmt: off

_N = np.array(
    [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27,
     28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45,
     46, 47, 48, 49, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 110, 120,
     130, 140]
)

_Kn = np.array(
    [2.036, 2.088, 2.134, 2.175, 2.213, 2.247, 2.279, 2.309, 2.335, 2.361,
     2.385, 2.408, 2.429, 2.448, 2.467, 2.486, 2.502, 2.519, 2.534, 2.549,
     2.563, 2.577, 2.591, 2.604, 2.616, 2.628, 2.639, 2.65, 2.661, 2.671,
     2.682, 2.692, 2.7, 2.71, 2.719, 2.727, 2.736, 2.744, 2.753, 2.76,
     2.768, 2.804, 2.837, 2.866, 2.893, 2.917, 2.94, 2.961, 2.981, 3,
     3.017, 3.049, 3.078, 3.104, 3.129]
)

# fmt: on

t_rel_Kn_n = pd.DataFrame(np.stack((_N, _Kn), axis=1), columns=["N", "Kn"])


def find_Kn(data_count=None, table=t_rel_Kn_n, **kwargs):
    """
    Find the value of Kn (Kurva N) based on the given data count.

    Parameters:
        data_count (int): The number of data points.
        table (pandas.DataFrame): The table containing the values of N and Kn.
        **kwargs: Additional keyword arguments.

    Returns:
        float: The interpolated value of Kn based on the data count.

    Raises:
        ValueError: If the data count is outside the range of 10 to 140.
    """

    # handle deprecated params
    data_count = handle_deprecated_params(kwargs, "n", "data_count") or data_count

    if data_count < 10 or data_count > 140:
        raise ValueError("Jumlah data diluar batas bawah (10) / batas atas (140)")

    N = table["N"].to_numpy()
    Kn = table["Kn"].to_numpy()
    return np.interp(data_count, N, Kn)


# Calculate lower/upper boundary for outlier test
def calc_boundary(
    dataframe=None,
    target_column=None,
    result_type="value",
    display_stat=False,
    **kwargs,
):
    """
    Calculate the boundary values for a given target column in a dataframe.

    Parameters:
    - dataframe: pandas DataFrame, optional (default=None)
        The input dataframe containing the target column.
    - target_column: str, optional (default=None)
        The name of the target column in the dataframe.
    - result_type: str, optional (default="value")
        The type of result to return. Possible values are "value" or "log".
    - display_stat: bool, optional (default=False)
        Whether to display the statistics of the calculation.

    Returns:
    - tuple
        A tuple containing the lower and higher boundary values.

    Raises:
    - ValueError
        If the result_type is not "value" or "log".
    """

    # handle deprecated params
    dataframe = handle_deprecated_params(kwargs, "df", "dataframe") or dataframe
    target_column = (
        handle_deprecated_params(kwargs, "col", "target_column") or target_column
    )
    result_type = (
        handle_deprecated_params(kwargs, "result", "result_type") or result_type
    )
    display_stat = (
        handle_deprecated_params(kwargs, "show_stat", "display_stat") or display_stat
    )

    target_column = dataframe.columns[0] if target_column is None else target_column

    x = dataframe[target_column].to_numpy()
    n = x.size
    xlog = np.log10(x)
    xlogmean = xlog.mean()
    xlogstd = xlog.std(ddof=1)

    Kn = find_Kn(n)

    # higher
    y_h = xlogmean + Kn * xlogstd
    val_h = 10**y_h

    # lower
    y_l = xlogmean - Kn * xlogstd
    val_l = 10**y_l

    if display_stat:
        print(
            "Statistik:",
            f"N = {n}",
            f"Mean (log) = {xlogmean:.5f}",
            f"Std (log) = {xlogstd:.5f}",
            f"Lower (val) = {val_l:.5f}",
            f"Higher (val) = {val_h:.5f}",
            sep="\n",
            end="\n\n",
        )

    if result_type.lower() == "value":
        return (val_l, val_h)
    if result_type.lower() == "log":
        return (y_l, y_h)
    raise ValueError("result_type harus 'value' atau 'log'.")


# calculate outlier
def find_outlier(dataframe=None, target_column=None, verbose=False, **kwargs):
    """
    Find outliers in a dataframe based on a target column.

    Args:
        dataframe (pandas.DataFrame): The input dataframe.
        target_column (str): The name of the target column to find outliers in.
        verbose (bool): Whether to print verbose output.
        **kwargs: Additional keyword arguments.

    Returns:
        pandas.DataFrame or None: A new dataframe with the target column and
            an "outlier" column indicating the type of outlier,
            or None if no outliers are found.
    """
    # deprecated params
    dataframe = handle_deprecated_params(kwargs, "df", "dataframe") or dataframe
    target_column = (
        handle_deprecated_params(kwargs, "col", "target_column") or target_column
    )

    low, high = calc_boundary(dataframe, target_column, **kwargs)

    target_column = dataframe.columns[0] if target_column is None else target_column

    masklow = dataframe[target_column] < low
    maskhigh = dataframe[target_column] > high
    mask = masklow | maskhigh

    if verbose and masklow.sum():
        print(f"Ada outlier dibawah batas bawah sebanyak {masklow.sum()}.")
    if verbose and maskhigh.sum():
        print(f"Ada outlier diatas batas atas sebanyak {maskhigh.sum()}.")

    def check_outlier(x):
        if x < low:
            return "lower"
        elif x > high:
            return "higher"
        return pd.NA

    if mask.sum() != 0:
        new_df = dataframe.copy()
        new_df["outlier"] = dataframe[target_column].apply(check_outlier)
        return new_df[[target_column, "outlier"]]

    print("Tidak ada Outlier")
    return None
