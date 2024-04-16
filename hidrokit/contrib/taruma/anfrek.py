"""
Modul rekap analisis frekuensi. Untuk manual lihat modul terpisah.
"""

import warnings
from hidrokit.contrib.taruma import gumbel, lognormal, logpearson3, normal

warnings.warn(
    "This module will be deprecated in the future. "
    "Please use speficic distribution modules such as "
    "normal, lognormal, logpearson3, and gumbel instead.",
    FutureWarning,
)


freq_normal = normal.freq_normal
freq_lognormal = lognormal.freq_lognormal
freq_logpearson3 = logpearson3.freq_logpearson3
freq_gumbel = gumbel.freq_gumbel
