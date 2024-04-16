"""
modul rekap untuk uji kecocokan distribusi
"""

import warnings
from hidrokit.contrib.taruma import chi_square, kolmogorov_smirnov

warnings.warn(
    "This module will be deprecated in the future. Please use kolmogorov_smirnov "
    "and chi_square modules instead.",
    FutureWarning,
)


uji_kstest = kolmogorov_smirnov.kolmogorov_smirnov_test
uji_chisquare = chi_square.chi_square_test
