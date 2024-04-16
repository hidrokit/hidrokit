"""
hk127: gumbel.py
=====================

Module for Gumbel distribution calculations.

This module provides functions for 
    calculating coefficients and K values based on the Gumbel distribution.
    It includes tables from different sources and methods for interpolation.

Functions:
- find_coef(n, source="gumbel"): Find the coefficient based on the given source.
- calc_K(data_count=None, return_periods=None, source="gumbel", display_stat=False, **kwargs):
    Calculate the K value using different methods based on the specified source.

Tables:
- t_gumbel_gb: Table of coefficients from Gumbel source (Gumbel, GB).
- t_gumbel_sw: Table of coefficients from Soewarno source (Gumbel, GB).
- t_gumbel_st: Table of coefficients from Soetopo source (Gumbel, GB).

manual:
    https://gist.github.com/taruma/ffa77e6f50a19fa5d05ab10e27d3266a
"""

import numpy as np
import pandas as pd
from scipy import stats
from hidrokit.contrib.taruma.utils import handle_deprecated_params

# tabel dari gumbel
# Statistics of Extremes oleh Gumbel p.228

# KODE: GB

# fmt: off

_DATA_GB = [
    [0.48430, 0.90430],
    [0.49020, 0.92880],
    [0.49520, 0.94970],
    [0.49960, 0.96760],
    [0.50350, 0.98330],
    [0.50700, 0.99720],
    [0.51000, 1.00950],
    [0.51280, 1.02057],
    [0.51570, 1.03160],
    [0.51810, 1.04110],
    [0.52020, 1.04930],
    [0.52200, 1.05660],
    [0.52355, 1.06283],
    [0.52520, 1.06960],
    [0.52680, 1.07540],
    [0.52830, 1.08110],
    [0.52960, 1.08640],
    [0.53086, 1.09145],
    [0.53200, 1.09610],
    [0.53320, 1.10040],
    [0.53430, 1.10470],
    [0.53530, 1.10860],
    [0.53622, 1.11238],
    [0.53710, 1.11590],
    [0.53800, 1.11930],
    [0.53880, 1.12260],
    [0.53960, 1.12550],
    [0.54034, 1.12847],
    [0.54100, 1.13130],
    [0.54180, 1.13390],
    [0.54240, 1.13630],
    [0.54300, 1.13880],
    [0.54362, 1.14132],
    [0.54420, 1.14360],
    [0.54480, 1.14580],
    [0.54530, 1.14800],
    [0.54580, 1.14990],
    [0.54630, 1.15185],
    [0.54680, 1.15380],
    [0.54730, 1.15570],
    [0.54770, 1.15740],
    [0.54810, 1.15900],
    [0.54854, 1.16066],
    [0.54890, 1.16230],
    [0.54930, 1.16380],
    [0.54970, 1.16530],
    [0.55010, 1.16670],
    [0.55040, 1.16810],
    [0.55080, 1.16960],
    [0.55110, 1.17080],
    [0.55150, 1.17210],
    [0.55180, 1.17340],
    [0.55208, 1.17467],
    [0.55270, 1.17700],
    [0.55330, 1.17930],
    [0.55380, 1.18140],
    [0.55430, 1.18340],
    [0.55477, 1.18536],
    [0.55520, 1.18730],
    [0.55570, 1.18900],
    [0.55610, 1.19060],
    [0.55650, 1.19230],
    [0.55688, 1.19382],
    [0.55720, 1.19530],
    [0.55760, 1.19670],
    [0.55800, 1.19800],
    [0.55830, 1.19940],
    [0.55860, 1.20073],
    [0.55890, 1.20200],
    [0.55920, 1.20320],
    [0.55950, 1.20440],
    [0.55980, 1.20550],
    [0.56002, 1.20649],
    [0.56461, 1.22534],
    [0.56715, 1.23598],
    [0.56878, 1.24292],
    [0.56993, 1.24786],
    [0.57144, 1.25450],
    [0.57240, 1.25880],
    [0.57377, 1.26506],
    [0.57450, 1.26851]
]

_INDEX_GB = (
    list(range(8, 61)) +
    list(range(62, 101, 2)) +
    list(range(150, 301, 50)) +
    [400, 500, 750, 1000]
)

_COL_GB = ['yn', 'sn']

t_gumbel_gb = pd.DataFrame(
    data=_DATA_GB, index=_INDEX_GB, columns=_COL_GB
)

# tabel dari soewarno
# Tabel 3.11A & 3.11B p.129-130

# KODE: GB

_DATA_SW = [
    [0.4592, 0.9496],
    [0.4996, 0.9676],
    [0.5053, 0.9933],
    [0.5070, 0.9971],
    [0.5100, 1.0095],
    [0.5128, 1.0206],
    [0.5157, 1.0316],
    [0.5181, 1.0411],
    [0.5202, 1.0493],
    [0.5220, 1.0565],
    [0.5236, 1.0628],
    [0.5252, 1.0696],
    [0.5268, 1.0754],
    [0.5283, 1.0811],
    [0.5296, 1.0864],
    [0.5309, 1.0915],
    [0.5320, 1.1961],
    [0.5332, 1.1004],
    [0.5343, 1.1047],
    [0.5353, 1.1086],
    [0.5362, 1.1124],
    [0.5371, 1.1159],
    [0.5380, 1.1193],
    [0.5388, 1.1226],
    [0.5396, 1.1255],
    [0.5402, 1.1285],
    [0.5410, 1.1313],
    [0.5418, 1.1339],
    [0.5424, 1.1363],
    [0.5430, 1.1388],
    [0.5436, 1.1413],
    [0.5442, 1.1436],
    [0.5448, 1.1458],
    [0.5453, 1.1480],
    [0.5458, 1.1499],
    [0.5463, 1.1519],
    [0.5468, 1.1538],
    [0.5473, 1.1557],
    [0.5477, 1.1574],
    [0.5481, 1.1590],
    [0.5485, 1.1607],
    [0.5489, 1.1623],
    [0.5493, 1.1638],
    [0.5497, 1.1658],
    [0.5501, 1.1667],
    [0.5504, 1.1681],
    [0.5508, 1.1696],
    [0.5511, 1.1708],
    [0.5518, 1.1721],
    [0.5518, 1.1734],
    [0.5521, 1.1747],
    [0.5524, 1.1759],
    [0.5527, 1.1770],
    [0.5530, 1.1782],
    [0.5533, 1.1793],
    [0.5535, 1.1803],
    [0.5538, 1.1814],
    [0.5540, 1.1824],
    [0.5543, 1.1834],
    [0.5545, 1.1844],
    [0.5548, 1.1854],
    [0.5550, 1.1863],
    [0.5552, 1.1873],
    [0.5555, 1.1881],
    [0.5557, 1.1890],
    [0.5559, 1.1898],
    [0.5561, 1.1906],
    [0.5563, 1.1915],
    [0.5565, 1.1923],
    [0.5567, 1.1930],
    [0.5569, 1.1938],
    [0.5570, 1.1945],
    [0.5572, 1.1953],
    [0.5574, 1.1959],
    [0.5576, 1.1967],
    [0.5578, 1.1973],
    [0.5580, 1.1980],
    [0.5581, 1.1987],
    [0.5583, 1.1994],
    [0.5585, 1.2001],
    [0.5586, 1.2007],
    [0.5587, 1.2013],
    [0.5589, 1.2020],
    [0.5591, 1.2026],
    [0.5592, 1.2032],
    [0.5593, 1.2038],
    [0.5595, 1.2044],
    [0.5596, 1.2049],
    [0.5598, 1.2055],
    [0.5599, 1.2060],
    [0.5600, 1.2065],
]

_INDEX_SW = list(range(10, 101))

_COL_SW = ['yn', 'sn']

t_gumbel_sw = pd.DataFrame(
    data=_DATA_SW, index=_INDEX_SW, columns=_COL_SW
)

# Tabel dari Soetopo hal. 98
# Tabel 12.1 Yn dan Sn Gumbel

# KODE: ST

_DATA_ST = [
    [0.4843, 0.9043],
    [0.4902, 0.9288],
    [0.4952, 0.9497],
    [0.4996, 0.9676],
    [0.5035, 0.9833],
    [0.5070, 0.9972],
    [0.5100, 1.0095],
    [0.5128, 1.0205],
    [0.5157, 1.0316],
    [0.5181, 1.0411],
    [0.5202, 1.0493],
    [0.5220, 1.0566],
    [0.5235, 1.0628],
    [0.5252, 1.0696],
    [0.5268, 1.0754],
    [0.5283, 1.0811],
    [0.5296, 1.0864],
    [0.5309, 1.0915],
    [0.5320, 1.0961],
    [0.5332, 1.1004],
    [0.5343, 1.1047],
    [0.5353, 1.1086],
    [0.5362, 1.1124],
    [0.5371, 1.1159],
    [0.5380, 1.1193],
    [0.5388, 1.1226],
    [0.5396, 1.1255],
    [0.5402, 1.1285],
    [0.5410, 1.1313],
    [0.5418, 1.1339],
    [0.5424, 1.1363],
    [0.5430, 1.1388],
    [0.5436, 1.1413],
    [0.5442, 1.1436],
    [0.5448, 1.1458],
    [0.5453, 1.1480],
    [0.5458, 1.1499],
    [0.5463, 1.1519],
    [0.5468, 1.1538],
    [0.5473, 1.1557],
    [0.5477, 1.1574],
    [0.5481, 1.1590],
    [0.5485, 1.1607],
    [0.5489, 1.1623],
    [0.5493, 1.1638],
    [0.5497, 1.1658],
    [0.5501, 1.1667],
    [0.5504, 1.1681],
    [0.5508, 1.1696],
    [0.5511, 1.1708],
    [0.5515, 1.1721],
    [0.5518, 1.1734],
    [0.5521, 1.1747],
    [0.5524, 1.1759],
    [0.5527, 1.1770],
    [0.5530, 1.1782],
    [0.5533, 1.1793],
    [0.5535, 1.1803],
    [0.5538, 1.1814],
    [0.5540, 1.1824],
    [0.5543, 1.1834],
    [0.5545, 1.1844],
    [0.5548, 1.1854],
    [0.5550, 1.1863],
    [0.5552, 1.1873],
    [0.5555, 1.1881],
    [0.5557, 1.1890],
    [0.5559, 1.1898],
    [0.5561, 1.1906],
    [0.5563, 1.1915],
    [0.5565, 1.1923],
    [0.5567, 1.1930],
    [0.5569, 1.1938],
    [0.5570, 1.1945],
    [0.5572, 1.1953],
    [0.5574, 1.1959],
    [0.5576, 1.1967],
    [0.5578, 1.1973],
    [0.5580, 1.1980],
    [0.5581, 1.1987],
    [0.5583, 1.1994],
    [0.5585, 1.2001],
    [0.5586, 1.2007],
    [0.5587, 1.2013],
    [0.5589, 1.2020],
    [0.5591, 1.2026],
    [0.5592, 1.2032],
    [0.5593, 1.2038],
    [0.5595, 1.2044],
    [0.5596, 1.2049],
    [0.5598, 1.2055],
    [0.5599, 1.2060],
    [0.5600, 1.2065],
]

_INDEX_ST = list(range(8, 101))

_COL_ST = ['yn', 'sn']

t_gumbel_st = pd.DataFrame(
    data=_DATA_ST, index=_INDEX_ST, columns=_COL_ST
)

# fmt: on

# pylint: disable=invalid-name


def _find_in_table(val, table, y_col=None, x_col=None):
    x = table.index if x_col is None else table[x_col]
    y = table.iloc[:, 0] if y_col is None else table[y_col]
    return np.interp(val, x, y)


def _find_Yn_Sn(n, table):
    yn = _find_in_table(n, table, y_col="yn")
    sn = _find_in_table(n, table, y_col="sn")
    return yn, sn


def find_coef(n, source="gumbel"):
    """
    Find the coefficient based on the given source.

    Parameters:
    - n (int): The coefficient value to find.
    - source (str): The source to use for finding the coefficient. Default is "gumbel".

    Returns:
    - The coefficient value based on the given source.

    Raises:
    - ValueError: If the given source is not found.
    """
    if source.lower() == "gumbel":
        return _find_Yn_Sn(n, t_gumbel_gb)
    if source.lower() == "soewarno":
        return _find_Yn_Sn(n, t_gumbel_sw)
    if source.lower() == "soetopo":
        return _find_Yn_Sn(n, t_gumbel_st)

    raise ValueError(f"source '{source}' not found")


# def calc_K(n, return_period, source="gumbel", show_stat=False):


def calc_K(
    data_count=None, return_periods=None, source="gumbel", display_stat=False, **kwargs
):
    """
    Calculate the K value using different methods based on the specified source.

    Parameters:
    - data_count (int): The number of data points.
    - return_periods (list or array-like): The return periods.
    - source (str): The source method to use for calculation. Options: 'gumbel', 'scipy', 'powell'.
    - display_stat (bool): Whether to display the calculated statistics.

    Returns:
    - K (array-like): The calculated K values.

    Raises:
    - ValueError: If the specified source is not found.
    """
    # handle deprecated params
    data_count = handle_deprecated_params(kwargs, "n", "data_count") or data_count
    return_periods = (
        handle_deprecated_params(kwargs, "return_period", "return_periods")
        or return_periods
    )
    display_stat = (
        handle_deprecated_params(kwargs, "show_stat", "display_stat") or display_stat
    )

    return_periods = np.array(return_periods)

    if source.lower() == "scipy":
        # perhitungan probabilitasnya belum dapat dipastikan formulanya
        prob = 1 - 1 / return_periods
        # prob = 1 - np.log(return_period/(return_period-1))
        return stats.gumbel_r.ppf(prob)
    if source.lower() == "powell":
        return (
            -np.sqrt(6)
            / np.pi
            * (np.euler_gamma + np.log(np.log(return_periods / (return_periods - 1))))
        )
    if source.lower() == "gumbel":
        # dibuku Soewarno dinyatakan T>=20 menggunakan
        # ln(T), tapi dicontohnya tidak mengikuti formula tersebut
        # jadi yang digunakan rumus umumnya saja.
        # if source.lower() == 'soewarno':
        #     yt = []
        #     for t in return_period:
        #         if t <= 20:
        #             yt += [-np.log(-np.log((t - 1)/t))]
        #         else:
        #             yt += [np.log(t)]
        #     yt = np.array(yt)
        # else:
        #     yt = -np.log(-np.log((return_period - 1)/return_period))

        yn, sn = find_coef(data_count, source=source)
        yt = -np.log(-np.log((return_periods - 1) / return_periods))
        K = (yt - yn) / sn

        if display_stat:
            print(f"y_n = {yn}")
            print(f"s_n = {sn}")
            print(f"y_t = {yt}")
        return K

    raise ValueError(f"source '{source}' not found")


def calc_x_gumbel(
    input_array=None, return_periods=None, source="gumbel", display_stat=False, **kwargs
):
    """
    Calculate the Gumbel distribution parameter 'x' based on the input array.

    Args:
        input_array (array-like): The input array of values.
        return_periods (list, optional): The list of return periods. Defaults to [5].
        source (str, optional): The source of the distribution. Defaults to "gumbel".
        display_stat (bool, optional): Whether to display the calculated statistics.
            Defaults to False.
        **kwargs: Additional keyword arguments for deprecated parameters.

    Returns:
        array-like: The calculated 'x' values based on the Gumbel distribution.

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

    data_mean = np.mean(input_array)
    data_std = np.std(input_array, ddof=1)
    data_count = len(input_array)

    k = calc_K(data_count, return_periods, source=source, display_stat=display_stat)

    if display_stat:
        print(f"x_mean = {data_mean:.5f}")
        print(f"x_std = {data_std:.5f}")
        print(f"k = {k}")

    x_values = data_mean + k * data_std
    return x_values


# def freq_gumbel(
#     df,
#     col=None,
#     return_period=[2, 5, 10, 20, 25, 50, 100],
#     source="gumbel",
#     show_stat=False,
#     col_name="Gumbel",
#     index_name="Kala Ulang",
# ):


def freq_gumbel(
    dataframe=None,
    target_column=None,
    return_periods=None,
    display_stat=False,
    source="gumbel",
    out_column_name="Gumbel",
    out_index_name="Kala Ulang",
    **kwargs,
):
    """
    Calculate the frequency analysis using the Gumbel distribution.

    Parameters:
    - dataframe (pandas.DataFrame): The input dataframe containing the data.
    - target_column (str): The name of the column in the dataframe to be analyzed.
        Default is None (first column of dataframe).
    - return_periods (list): The list of return periods to calculate.
        Default is None ([5]).
    - display_stat (bool): Whether to display the statistical information.
        Default is False.
    - source (str): The source of the distribution.
        Default is 'gumbel'.
    - out_column_name (str): The name of the output column in the result dataframe.
        Default is 'Gumbel'.
    - out_index_name (str): The name of the index in the result dataframe.
        Default is 'Kala Ulang'.
    - **kwargs: Additional keyword arguments for deprecated parameters.

    Deprecated Parameters:
    - df (pandas.DataFrame):
        Deprecated parameter for 'dataframe'. Use 'dataframe' instead.
    - col (str):
        Deprecated parameter for 'target_column'. Use 'target_column' instead.
    - return_period (list):
        Deprecated parameter for 'return_periods'. Use 'return_periods' instead.
    - show_stat (bool):
        Deprecated parameter for 'display_stat'. Use 'display_stat' instead.
    - col_name (str):
        Deprecated parameter for 'out_column_name'. Use 'out_column_name' instead.
    - index_name (str):
        Deprecated parameter for 'out_index_name'. Use 'out_index_name' instead.

    Returns:
    - pandas.DataFrame: The result dataframe containing the calculated values.

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

    arr = calc_x_gumbel(
        x, return_periods=return_periods, display_stat=display_stat, source=source
    )

    result = pd.DataFrame(data=arr, index=return_periods, columns=[out_column_name])

    result.index.name = out_index_name
    return result


def _calc_T(P):
    return 1 / (1 - np.exp(-np.exp(-P)))


def _calc_prob_from_table(k, n, source="gumbel"):
    yn, sn = find_coef(n, source=source)
    P = k * sn + yn
    T = _calc_T(P)
    return np.around(1 - 1 / T, 3)


def calc_prob(k_values=None, data_count=None, source="gumbel", **kwargs):
    """
    Calculate the probability using different sources.

    Parameters:
        k_values (array-like): The values of k.
        data_count (int): The count of data.
        source (str): The source to calculate the probability from.
                      Options: "gumbel", "soewarno", "soetopo", "scipy", "powell".
                      Default is "gumbel".
        **kwargs: Additional keyword arguments.

    Returns:
        The calculated probability.

    Deprecated Parameters:
        k (array-like): Deprecated. Use k_values instead.
        n (int): Deprecated. Use data_count instead.
    """

    # handle deprecated params
    k_values = handle_deprecated_params(kwargs, "k", "k_values") or k_values
    data_count = handle_deprecated_params(kwargs, "n", "data_count") or data_count

    if source.lower() == "gumbel":
        return _calc_prob_from_table(k_values, data_count, source=source)
    if source.lower() == "soewarno":
        return _calc_prob_from_table(k_values, data_count, source=source)
    if source.lower() == "soetopo":
        return _calc_prob_from_table(k_values, data_count, source=source)
    if source.lower() == "scipy":
        return stats.gumbel_r.cdf(k_values)
    if source.lower() == "powell":
        # persamaan ini ditemukan menggunakan wolfram alpha
        # x = e^(e^(-(π K)/sqrt(6) - p))/(e^(e^(-(π K)/sqrt(6) - p)) - 1)
        _top = np.exp(np.exp(-(np.pi * k_values) / np.sqrt(6) - np.euler_gamma))
        _bot = _top - 1
        T = _top / _bot
        return 1 - 1 / T
    raise ValueError(f"source '{source}' not found")