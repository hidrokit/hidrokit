"""
Modul rekap analisis frekuensi. Untuk manual lihat modul terpisah.
"""

import warnings
from hidrokit.contrib.taruma import hk172, hk124, hk126, hk127

warnings.warn(
    "This module will be deprecated in the future. "
    "Please use speficic distribution modules such as "
    "normal, lognormal, logpearson3, and gumbel instead.",
    FutureWarning,
)


freq_normal = hk172.freq_normal
freq_lognormal = hk124.freq_lognormal
freq_logpearson3 = hk126.freq_logpearson3
freq_gumbel = hk127.freq_gumbel

normal = hk172
lognormal = hk124
logpearson3 = hk126
gumbel = hk127
