"""
0.3.2
hk43 | Pivot Table
hk53 | Tensor Input RNN/LSTM
hk73 | BMKG

0.3.3
hk79 | Excel Jam-Jaman

0.3.4
hk84 | Ringkasan Jam-Jaman

0.3.5
hk87 | Perhitungan Debit Andalan Menggunakan Kurva Durasi Debit
hk88 | Baca Dataset Harian
hk89 | Model NRECA
hk90 | Kalibrasi Model
hk96 | Model FJMock
hk98 | Rekap Deret Waktu
hk99 | Poligon Thiessen
hk106 | Evapotranspirasi

0.3.7
hk102 | Upsampling (kelupaan)
hk124 | Anfrek: Log Normal
hk126 | Anfrek: Log Pearson 3
hk127 | Anfrek: Gumbel
hk140 | Uji Kolmogorov-Smirnov
hk141 | Uji Chi-Square
hk151 | Uji Outlier
hk158 | Parameter Statistik
hk172 | Anfrek: Normal

anfrek | analisis frekuensi (normal, lognormal, logpearson3, gumbel)
"""

__all__ = [
    "hk53",
    "hk73",
    "hk79",
    "hk84",
    "hk87",
    "hk88",
    "hk89",
    "hk90",
    "hk96",
    "hk98",
    "hk99",
    "hk102",
    "hk106",
    "hk124",
    "hk126",
    "hk127",
    "hk140",
    "hk141",
    "hk151",
    "hk158",
    "hk172",
    "pamarayan_excel_data_extraction",
]


import warnings
import importlib

warnings.filterwarnings('default')

deprecated_modules = {
    "hk43": "pamarayan_excel_data_extraction",
}


def __getattr__(name):
    if name in deprecated_modules:
        warnings.warn(
            f"{name} is deprecated, use {deprecated_modules[name]} instead",
            DeprecationWarning,
        )
        new_module_name = deprecated_modules[name]
        new_module = importlib.import_module('.' + new_module_name, __name__)
        return new_module
    raise AttributeError(f"module {__name__} has no attribute {name}")
