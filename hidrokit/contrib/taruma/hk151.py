"""manual:
https://gist.github.com/taruma/7bf2e4e1601ab8390d9919043eb87682"""

import numpy as np
import pandas as pd

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

t_rel_Kn_n = pd.DataFrame(np.stack((_N, _Kn), axis=1), columns=['N', 'Kn'])

def find_Kn(n, table=t_rel_Kn_n):
    if n < 10 or n > 140:
        raise ValueError('Jumlah data diluar batas bawah (10) / batas atas (140)')
    else:
        N = table['N'].to_numpy()
        Kn = table['Kn'].to_numpy()
        return np.interp(n, N, Kn)

def calc_boundary(df, col=None, result='value', show_stat=False):
    col = df.columns[0] if col is None else col
    
    x = df[col].to_numpy()
    n = x.size
    xlog = np.log10(x)
    xlogmean = xlog.mean()
    xlogstd = xlog.std(ddof=1)

    Kn = find_Kn(n)

    # higher
    y_h = xlogmean + Kn*xlogstd
    val_h = 10**y_h

    # lower
    y_l = xlogmean - Kn*xlogstd
    val_l = 10**y_l

    if show_stat:
        print(
            f'Statistik:',
            f'N = {n}',
            f'Mean (log) = {xlogmean:.5f}',
            f'Std (log) = {xlogstd:.5f}',
            f'Lower (val) = {val_l:.5f}',
            f'Higher (val) = {val_h:.5f}',
            sep='\n', end='\n\n'
        )

    if result.lower() == 'value':
        return (val_l, val_h)
    elif result.lower() == 'log':
        return (y_l, y_h)

def find_outlier(df, col=None, verbose=False, **kwargs):
    
    low, high = calc_boundary(df, col, **kwargs)
    
    col = df.columns[0] if col is None else col

    masklow = df[col] < low
    maskhigh = df[col] > high
    mask = masklow | maskhigh
    
    if verbose and masklow.sum():
        print(f'Ada outlier dibawah batas bawah sebanyak {masklow.sum()}.')
    if verbose and maskhigh.sum():
        print(f'Ada outlier diatas batas atas sebanyak {maskhigh.sum()}.')

    def check_outlier(x):
        if x < low:
            return "lower"
        elif x > high:
            return "higher"
        else:
            return pd.NA

    if mask.sum() != 0:
        new_df = df.copy()
        new_df['outlier'] = df[col].apply(check_outlier)
        return new_df[[col, 'outlier']]
    else:
        print("Tidak ada Outlier")
        return None
