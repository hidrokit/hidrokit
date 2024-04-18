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
"""

__all__ = [
    "bmkg_utils",
    "chi_square",
    "dataframe_to_tensor",
    "dependable_flow",
    "evapotranspiration",
    "fjmock_model",
    "gumbel",
    "hidrokit_excel_parser",
    "hidrokit_hourly_excel_parser",
    "kolmogorov_smirnov",
    "lognormal",
    "logpearson3",
    "model_calibration",
    "normal",
    "nreca_model",
    "outlier_hydrology",
    "pamarayan_excel_data_extraction",
    "statistical_coefficients",
    "statistic_summary",
    "summary_hourly",
    "thiessen",
    "upsampling",
    "utils",
]


import warnings
import importlib

deprecated_modules = {
    "hk43": "pamarayan_excel_data_extraction",
    "hk53": "dataframe_to_tensor",
    "hk73": "bmkg_utils",
    "hk79": "hidrokit_hourly_excel_parser",
    "hk84": "summary_hourly",
    "hk87": "dependable_flow",
    "hk88": "hidrokit_excel_parser",
    "hk89": "nreca_model",
    "hk90": "model_calibration",
    "hk96": "fjmock_model",
    "hk98": "statistic_summary",
    "hk99": "thiessen",
    "hk102": "upsampling",
    "hk106": "evapotranspiration",
    "hk124": "lognormal",
    "hk126": "logpearson3",
    "hk127": "gumbel",
    "hk140": "kolmogorov_smirnov",
    "hk141": "chi_square",
    "hk151": "outlier_hydrology",
    "hk158": "statistical_coefficients",
    "hk172": "normal",
}


def __getattr__(name):
    if name in deprecated_modules:
        warnings.warn(
            f"{name} is deprecated, use {deprecated_modules[name]} instead",
            FutureWarning,
        )
        new_module_name = deprecated_modules[name]
        new_module = importlib.import_module("." + new_module_name, __name__)
        return new_module
    raise AttributeError(f"module {__name__} has no attribute {name}")
