"""manual:
https://gist.github.com/taruma/5d3ab88893e56f895dc3f36ea19c3e60"""

import numpy as np
import pandas as pd
from scipy import stats

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

def _find_k_in_table(return_period, table):
    x = table.periode_ulang
    y = table.k
    return np.interp(return_period, x, y)

def find_K(return_period, source='scipy'):
    if source.lower() == 'soewarno':
        return _find_k_in_table(return_period, t_normal_sw)
    elif source.lower() == 'scipy':
        return_period = np.array(return_period)
        return stats.norm.ppf(1 - 1/return_period)

def calc_x_lognormal(x, return_period=[5], source='scipy', show_stat=False):
    return_period = np.array(return_period)
    y = np.log10(x)
    y_mean = np.mean(y)
    y_std = np.std(y, ddof=1)
    n = len(y)

    k = find_K(return_period, source=source)

    if show_stat:
        print(f'y_mean = {y_mean:.5f}')
        print(f'y_std = {y_std:.5f}')
        print(f'k = {k}')

    val_y = y_mean + k * y_std
    val_x = np.power(10, val_y)
    return val_x

def freq_lognormal(
    df, col=None,
    return_period=[2, 5, 10, 20, 25, 50, 100], show_stat=False, source='scipy',
    col_name='Log Normal'):

    col = df.columns[0] if col is None else col

    x = df[col].copy()

    arr = calc_x_lognormal(
        x, return_period=return_period, show_stat=show_stat, source=source)

    return pd.DataFrame(
        data=arr, index=return_period, columns=[col_name]
    )

def _calc_prob_in_table(k, table):
    x = table.k
    y = table.peluang
    return np.interp(k, x, y)

def calc_prob(k, source='scipy'):
    if source.lower() == 'soewarno':
        k = np.array(k)
        return 1 - _calc_prob_in_table(k, t_normal_sw)
    elif source.lower() == 'scipy':
        return stats.norm.cdf(k)
