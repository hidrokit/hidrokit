"""manual:
https://gist.github.com/taruma/5d16baf90016d8a08c6870b674226691"""

import numpy as np
import pandas as pd
from scipy import stats
from hidrokit.contrib.taruma import hk172, hk124, hk127, hk126 

frek_normal, frek_lognormal, frek_gumbel, frek_logpearson3 = hk172, hk124, hk127, hk126

# tabel dari soetopo hal. 139
# Tabel Nilai Kritis (Dcr) Untuk Uji Kolmogorov-Smirnov

# KODE: ST

_DATA_ST = [
    [0.900, 0.925, 0.950, 0.975, 0.995],
    [0.684, 0.726, 0.776, 0.842, 0.929],
    [0.565, 0.597, 0.642, 0.708, 0.829],
    [0.494, 0.525, 0.564, 0.624, 0.734],
    [0.446, 0.474, 0.510, 0.563, 0.669],
    [0.410, 0.436, 0.470, 0.521, 0.618],
    [0.381, 0.405, 0.438, 0.486, 0.577],
    [0.358, 0.381, 0.411, 0.457, 0.543],
    [0.339, 0.360, 0.388, 0.432, 0.514],
    [0.322, 0.342, 0.368, 0.409, 0.486],
    [0.307, 0.326, 0.352, 0.391, 0.468],
    [0.295, 0.313, 0.338, 0.375, 0.450],
    [0.284, 0.302, 0.325, 0.361, 0.433],
    [0.274, 0.292, 0.314, 0.349, 0.418],
    [0.266, 0.283, 0.304, 0.338, 0.404],
    [0.258, 0.274, 0.295, 0.328, 0.391],
    [0.250, 0.266, 0.286, 0.318, 0.380],
    [0.244, 0.259, 0.278, 0.309, 0.370],
    [0.237, 0.252, 0.272, 0.301, 0.361],
    [0.231, 0.246, 0.264, 0.294, 0.352],
]

_INDEX_ST = range(1, 21)

_COL_ST = [0.2, 0.15, 0.1, 0.05, 0.01]

t_dcr_st = pd.DataFrame(
    data=_DATA_ST, index=_INDEX_ST, columns=_COL_ST
)

# tabel dari soewarno hal. 139
# Tabel Nilai Kritis (Dcr) Untuk Uji Kolmogorov-Smirnov

# KODE: SW

_DATA_SW = [
    [0.45, 0.51, 0.56, 0.67],
    [0.32, 0.37, 0.41, 0.49],
    [0.27, 0.3 , 0.34, 0.4 ],
    [0.23, 0.26, 0.29, 0.35],
    [0.21, 0.24, 0.26, 0.32],
    [0.19, 0.22, 0.24, 0.29],
    [0.18, 0.2 , 0.22, 0.27],
    [0.17, 0.19, 0.21, 0.25],
    [0.16, 0.18, 0.2 , 0.24],
    [0.15, 0.17, 0.19, 0.23]
]

_INDEX_SW = range(5, 51, 5)

_COL_SW = [0.2, 0.1, 0.05, 0.01]

t_dcr_sw = pd.DataFrame(
    data=_DATA_SW, index=_INDEX_SW, columns=_COL_SW
)

# KODE FUNGSI INTERPOLASI DARI TABEL

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

def _calc_k(x):
    return (x - x.mean()) / x.std()

table_source = {
    'soewarno': t_dcr_sw,
    'soetopo': t_dcr_st
}

anfrek = {
    'normal': frek_normal,
    'lognormal': frek_lognormal,
    'gumbel': frek_gumbel,
    'logpearson3': frek_logpearson3
}

def calc_dcr(alpha, n, source='scipy'):
    alpha = np.array(alpha)
    if source.lower() == 'scipy':
        # ref: https://stackoverflow.com/questions/53509986/
        return stats.ksone.ppf(1-alpha/2, n)
    elif source.lower() in table_source.keys():
        func_table = _func_interp_bivariate(table_source[source.lower()])
        # untuk soewarno 2 angka dibelakang koma, dan soetopo = 3
        dec = (source.lower() == 'soetopo') + 2
        return _as_value(func_table(n, alpha, grid=False), dec)

def kstest(
    df, col=None, dist='normal', source_dist=None, 
    alpha=0.05, source_dcr='scipy', show_stat=True, report='result'
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
    data = data.sort_values('x')
    data['no'] = np.arange(n) + 1

    # w = weibull
    data['p_w'] = data.no / (n+1)
    
    if dist.lower() in ['normal', 'gumbel']:
        data['k'] = _calc_k(data.x)
    if dist.lower() in ['lognormal', 'logpearson3']:
        data['log_x'] = np.log10(data.x)
        data['k'] = _calc_k(data.log_x)

    func = anfrek[dist.lower()]

    if dist.lower() in ['normal', 'lognormal']:
        parameter = ()
    elif dist.lower() == 'gumbel':
        parameter = (n,)
    elif dist.lower() == 'logpearson3':
        parameter = (data.log_x.skew(),)
    
    # d = distribusi
    data['p_d'] = func.calc_prob(data.k, source=source_dist, *parameter) 
    data['d'] = (data.p_w - data.p_d).abs()
    dmax = data.d.max()
    dcr = calc_dcr(alpha, n, source=source_dcr)
    result = int(dmax < dcr)
    result_text = ['Distribusi Tidak Diterima', 'Distribusi Diterima']

    if show_stat:
        print(f'Periksa Kecocokan Distribusi {dist.title()}')
        print(f'Delta Kritikal = {dcr:.5f}')
        print(f'Delta Max = {dmax:.5f}')
        print(f'Result (Dmax < Dcr) = {result_text[result]}')

    if report.lower() == 'result':
        return data['no x p_w p_d d'.split()]
    elif report.lower() == 'full':
        return data
