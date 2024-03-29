"""manual:
https://gist.github.com/taruma/e250ab2685ba5b4c8facbf498cfb5cd8"""

import numpy as np
import pandas as pd
from scipy import stats
from hidrokit.contrib.taruma import hk172, hk124, hk127, hk126 

frek_normal, frek_lognormal, frek_gumbel, frek_logpearson3 = hk172, hk124, hk127, hk126

# tabel dari limantara hal. 117
# Tabel Nilai Kritis untuk Distribusi Chi Square (X^2)

# KODE: LM

_DATA_LM = [
    [0.039, 0.016, 0.698, 0.393, 3.841, 5.024, 6.635, 7.879],
    [0.100, 0.201, 0.506, 0.103, 5.991, 0.738, 9.210, 10.597],
    [0.717, 0.115, 0.216, 0.352, 7.815, 9.348, 11.345, 12.838],
    [0.207, 0.297, 0.484, 0.711, 9.488, 11.143, 13.277, 14.860],
    [0.412, 0.554, 0.831, 1.145, 11.070, 12.832, 15.086, 16.750],
    [0.676, 0.872, 1.237, 1.635, 12.592, 14.449, 16.812, 18.548],
    [0.989, 1.239, 1.690, 2.167, 14.067, 16.013, 18.475, 20.278],
    [1.344, 1.646, 2.180, 2.733, 15.507, 17.535, 20.090, 21.955],
    [1.735, 2.088, 2.700, 3.325, 16.919, 19.023, 21.666, 23.589],
    [2.156, 2.558, 3.247, 3.940, 18.307, 20.483, 23.209, 25.188],
    [2.603, 3.053, 3.816, 4.575, 19.675, 21.920, 24.725, 26.757],
    [3.074, 3.571, 4.404, 5.226, 21.026, 23.337, 26.217, 28.300],
    [3.565, 4.107, 5.009, 5.892, 22.362, 24.736, 27.688, 29.819],
    [4.075, 4.660, 5.629, 6.571, 23.685, 26.119, 29.141, 31.319],
    [4.601, 5.229, 6.262, 7.261, 24.996, 27.488, 30.578, 32.801],
    [5.142, 5.812, 6.908, 7.962, 26.296, 28.845, 32.000, 34.267],
    [5.697, 6.408, 7.564, 8.672, 27.587, 30.191, 33.409, 35.718],
    [6.265, 7.015, 8.231, 9.390, 28.869, 31.526, 34.805, 37.156],
    [6.884, 7.633, 8.907, 10.117, 30.144, 32.852, 36.191, 38.582],
    [7.434, 8.260, 9.591, 10.851, 31.410, 34.170, 37.566, 39.997],
    [8.034, 8.897, 10.283, 11.591, 32.671, 35.479, 38.932, 41.401],
    [8.643, 9.542, 10.982, 12.338, 33.924, 36.781, 40.289, 42.796],
    [9.260, 10.196, 11.689, 13.091, 36.172, 38.076, 41.638, 44.181],
    [9.886, 10.856, 12.401, 13.848, 36.415, 39.364, 42.980, 45.558],
    [10.520, 11.524, 13.120, 14.611, 37.652, 40.646, 44.314, 46.928],
    [11.160, 12.198, 13.844, 15.379, 38.885, 41.923, 45.642, 48.290],
    [11.808, 12.879, 14.573, 16.151, 40.113, 43.194, 46.963, 49.645],
    [12.461, 13.565, 15.308, 16.928, 41.337, 44.461, 48.278, 50.993],
    [13.121, 14.256, 16.047, 17.708, 42.557, 45.722, 49.588, 52.336],
    [13.787, 14.953, 16.791, 18.493, 43.773, 46.979, 50.892, 53.672],
]

_INDEX_LM = range(1, 31)

_COL_LM = [0.995, .99, .975, .95, .05, .025, 0.01, 0.005]

t_chi_lm = pd.DataFrame(
    data=_DATA_LM, index=_INDEX_LM, columns=_COL_LM
)

from scipy import interpolate

def _func_interp_bivariate(df):
    "Membuat fungsi dari tabel untuk interpolasi bilinear"
    table = df[df.columns.sort_values()].sort_index().copy()

    x = table.index
    y = table.columns
    z = table.to_numpy()

    # penggunaan kx=1, ky=1 untuk interpolasi linear antara 2 titik
    # tidak menggunakan (cubic) spline interpolation
    return interpolate.RectBivariateSpline(x, y, z, kx=1, ky=1)

def _as_value(x, dec=4):
    x = np.around(x, dec)
    return x.flatten() if x.size > 1 else x.item()

table_source = {
    'limantara': t_chi_lm
}

anfrek = {
    'normal': frek_normal.calc_x_normal,
    'lognormal': frek_lognormal.calc_x_lognormal,
    'gumbel': frek_gumbel.calc_x_gumbel,
    'logpearson3': frek_logpearson3.calc_x_lp3,
}

def _calc_k(n):
    return np.floor(1 + 3.22 * np.log10(n)).astype(int)

def _calc_dk(k, m):
    return k - 1 - m

def calc_xcr(alpha, dk, source='scipy'):
    alpha = np.array(alpha)

    if source.lower() in table_source.keys():
        func_table = _func_interp_bivariate(table_source[source.lower()])
        return _as_value(func_table(dk, alpha, grid=False), 3)
    if source.lower() == 'scipy':
        #ref: https://stackoverflow.com/questions/32301698
        return stats.chi2.isf(alpha, dk)

def chisquare(
    df, col=None, dist='normal', source_dist=None,
    alpha=0.05, source_xcr='scipy', show_stat=True,
    ):

    if source_dist is None:
        source_dist = (
            "scipy"
            if dist.lower() in ["normal", "lognormal", "logpearson3"]
            else "gumbel"
        )


    col = df.columns[0] if col is None else col
    data = df[[col]].copy()
    n = len(data)
    data = data.rename({col: 'x'}, axis=1)

    if dist.lower() in ['lognormal', 'logpearson3']:
        data['log_x'] = np.log10(data.x)

    k = _calc_k(n)
    prob_class = 1 / k
    prob_list = np.linspace(0, 1, k+1)[::-1]
    prob_seq = prob_list[1:-1]

    func = anfrek[dist.lower()]

    T = 1 / prob_seq
    val_x = func(data.x, return_period=T, source=source_dist)

    # Chi Square Table
    calc_df = pd.DataFrame()
    min = data.x.min()
    max = data.x.max()
    seq_x = np.concatenate([[min], val_x, [max]])

    calc_df['no'] = range(1, k+1)

    class_text = []
    for i in range(seq_x.size-1):
        if i == 0:
            class_text += [f'X <= {seq_x[i+1]:.4f}']
        elif i == seq_x.size-2:
            class_text += [f'X > {seq_x[i]:.4f}']
        else:
            class_text += [f'{seq_x[i]:.4f} < X <= {seq_x[i+1]:.4f}']
    calc_df['batas_kelas'] = class_text

    # calculate fe
    fe = []
    for i in range(seq_x.size-1):
        if i == 0:
            fe += [(data.x <= seq_x[i+1]).sum()]
        elif i == seq_x.size-2:
            fe += [(data.x > seq_x[i]).sum()]
        else:
            fe += [data.x.between(seq_x[i], seq_x[i+1], inclusive='right').sum()]
    calc_df['fe'] = fe

    ft = prob_class * n
    calc_df['ft'] = [ft]*k

    if dist.lower() in ['normal', 'gumbel', 'lognormal']:
        dk = _calc_dk(k, 2)
    elif dist.lower() in ['logpearson3']:
        # di buku soetopo nilai m nya diberi angka 3
        dk = _calc_dk(k, 2)

    X_calc = np.sum(np.power(2, (calc_df.fe-calc_df.ft))/calc_df.ft)
    X_critical = calc_xcr(alpha=alpha, dk=dk, source=source_xcr)
    result = int(X_calc < X_critical)
    result_text = ['Distribusi Tidak Diterima', 'Distribusi Diterima']
    calc_df.set_index('no', inplace=True)

    if show_stat:
        print(f'Periksa Kecocokan Distribusi {dist.title()}')
        print(f'Jumlah Kelas = {k}')
        print(f'Dk = {dk}')
        print(f'X^2_hitungan = {X_calc:.3f}')
        print(f'X^2_kritis = {X_critical:.3f}')
        print(f'Result (X2_calc < X2_cr) = {result_text[result]}')

    return calc_df
