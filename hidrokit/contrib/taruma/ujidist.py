"""
modul rekap untuk uji kecocokan distribusi
"""

import warnings
from hidrokit.contrib.taruma import hk140, hk141

warnings.warn(
    "This module will be deprecated in the future. Please use kolmogorov_smirnov "
    "and chi_square modules instead.",
    FutureWarning,
)


uji_kstest = hk140.kolmogorov_smirnov_test
uji_chisquare = hk141.chi_square_test
