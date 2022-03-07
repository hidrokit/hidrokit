"""manual:
https://gist.github.com/taruma/6a0b0f9dd26359f6832fe12bab30fdc7"""

import numpy as np
import pandas as pd

def _var(x):
    n = x.size
    return ((x-x.mean())**2).sum()/(n-1)

def _std(x):
    return np.sqrt(_var(x))

def _momen(x, r):
    n = x.size
    return 1/n * ((x-x.mean())**r).sum()

def _skew(x):
    n = x.size
    return n**2 / ((n-1)*(n-2)) * _momen(x, 3) / _std(x)**3

def _kurt(x):
    n = x.size
    return n**3 / ((n-1)*(n-2)*(n-3)) * _momen(x, 4) / _std(x)**4

def _Cv(x):
    return _std(x) / x.mean()

def calc_coef(x):
    """Return (Cv, Cs, Ck)"""
    return (_Cv(x), _skew(x), _kurt(x))

def check_distribution(x, show_stat=False):

    Cv, Cs, Ck = calc_coef(x)

    if show_stat:
        print(
            f'Cv = {Cv:.5f}',
            f'Cs = {Cs:.5f}',
            f'Ck = {Ck:.5f}',
            sep='\n', end='\n'
        )

    b_normal = True if np.isclose(Cs, 0, atol=0.1) and np.isclose(Ck, 3, atol=0.1) else False
    b_lognormal = True if np.isclose(Cs, 3, atol=0.1) and np.greater(Cs, 0) and np.isclose(Cs, 3*Cv, atol=0.1) else False
    b_gumbel = True if np.isclose(Cs, 1.1396, atol=0.0001) and np.isclose(Ck, 5.4002, atol=0.0001) else False
    b_logpearson = True #selalu benar terlepas nilai Cv, Cs, Ck

    _kriteria = lambda x: "Memenuhi" if x else "Tidak Memenuhi"

    print(
        f'{"Normal":<20}: {_kriteria(b_normal)}',
        f'{"Log Normal":<20}: {_kriteria(b_lognormal)}',
        f'{"Gumbel Tipe I":<20}: {_kriteria(b_gumbel)}',
        f'{"Log Pearson Tipe III":<20}: {_kriteria(b_logpearson)}',
        sep='\n', end='\n'
    )