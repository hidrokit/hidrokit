"""
modul rekap untuk uji kecocokan distribusi
"""

from hidrokit.contrib.taruma import hk140, hk141

uji_kstest = hk140.kolmogorov_smirnov_test
uji_chisquare = hk141.chi_square_test
