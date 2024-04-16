"""
hk158: statistical_coefficients.py

This module contains functions for calculating statistical coefficients and 
    checking the distribution of an input array.

Functions:
- calc_coef(x): Calculate the 
    coefficient of variation (Cv), skewness (Cs), and kurtosis (Ck) of an input array.
- check_distribution(input_array, display_stat=False, display_detail=False, **kwargs): 
    Check the distribution of an input array 
    and display the distribution statistics and details.

For more information, refer to the manual: 
    https://gist.github.com/taruma/6a0b0f9dd26359f6832fe12bab30fdc7
"""

import numpy as np
from hidrokit.contrib.taruma.utils import handle_deprecated_params

# pylint: disable=invalid-name


def _var(x):
    n = x.size
    return ((x - x.mean()) ** 2).sum() / (n - 1)


def _std(x):
    return np.sqrt(_var(x))


def _momen(x, r):
    n = x.size
    return 1 / n * ((x - x.mean()) ** r).sum()


def _skew(x):
    n = x.size
    return n**2 / ((n - 1) * (n - 2)) * _momen(x, 3) / _std(x) ** 3


def _kurt(x):
    n = x.size
    return n**3 / ((n - 1) * (n - 2) * (n - 3)) * _momen(x, 4) / _std(x) ** 4


def _Cv(x):
    return _std(x) / x.mean()


def calc_coef(x):
    """Return (Cv, Cs, Ck)"""
    return (_Cv(x), _skew(x), _kurt(x))


# def check_distribution(x, show_stat=False, show_detail=False):
# check if data fit with specific distribution
def check_distribution(
    input_array=None, display_stat=False, display_detail=False, **kwargs
):
    """
    Check the distribution of an input array.

    Parameters:
    - input_array (array-like): The input array to be checked.
    - display_stat (bool, optional): Whether to display the distribution statistics.
        Default is False.
    - display_detail (bool, optional): Whether to display the detailed information about
        each distribution. Default is False.
    - **kwargs: Additional keyword arguments.
        Deprecated parameters
            'x', 'show_stat', and 'show_detail' can be passed as keyword arguments.

    Returns:
    - None

    """

    # handle deprecated params
    input_array = handle_deprecated_params(kwargs, "x", "input_array") or input_array
    display_stat = (
        handle_deprecated_params(kwargs, "show_stat", "display_stat") or display_stat
    )
    display_detail = (
        handle_deprecated_params(kwargs, "show_detail", "display_detail")
        or display_detail
    )

    Cv, Cs, Ck = calc_coef(input_array)

    if display_stat:
        print(f"Cv = {Cv:.5f}", f"Cs = {Cs:.5f}", f"Ck = {Ck:.5f}", sep="\n", end="\n")

    b_normal = np.isclose(Cs, 0, atol=0.1) and np.isclose(Ck, 3, atol=0.1)
    b_lognormal = (
        np.isclose(Cs, 3, atol=0.1)
        and np.greater(Cs, 0)
        and np.isclose(Cs, 3 * Cv, atol=0.1)
    )
    b_gumbel = np.isclose(Cs, 1.1396, atol=0.0001) and np.isclose(
        Ck, 5.4002, atol=0.0001
    )
    b_logpearson = True  # selalu benar terlepas nilai Cv, Cs, Ck

    def _kriteria(x):
        return "Memenuhi" if x else "Tidak Memenuhi"

    print(
        f'{"Normal":<20}: {_kriteria(b_normal)}',
        f'{"Log Normal":<20}: {_kriteria(b_lognormal)}',
        f'{"Gumbel Tipe I":<20}: {_kriteria(b_gumbel)}',
        f'{"Log Pearson Tipe III":<20}: {_kriteria(b_logpearson)}',
        sep="\n",
        end="\n",
    )

    if display_detail:
        print(
            "-----------------------------------------------",
            "> Distribusi Normal [syarat](nilai)",
            f"[Cs ~ 0](Cs = {Cs:.5f})",
            f"[Ck ~ 3](Ck = {Ck:.5f})",
            "> Log Normal",
            f"[Cs ~ 3](Cs = {Cs:.5f})",
            f"[Cs > 0](Cs = {Cs:.5f})",
            f"[Cs ~ 3Cv](Cs = {Cs:.5f} ~ 3Cv = {3*Cv:.5f})",
            "> Gumbel Tipe I",
            f"[Cs ~ 1.1396](Cs = {Cs:.5f})",
            f"[Ck ~ 5.4002](Ck = {Ck:.5f})",
            "> Log Pearson Tipe III",
            "Tidak memiliki ciri khas (Cs/Ck/Cv = Bebas)",
            "-----------------------------------------------",
            sep="\n",
            end="\n",
        )

    return None
