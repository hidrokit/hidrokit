"""
hk126: logpearson3.py
==========================

This module provides functions for performing frequency analysis using 
    the Log-Pearson Type III distribution.

The Log-Pearson Type III distribution is a commonly used statistical 
    distribution for modeling extreme events, such as floods, droughts, and rainfall. 

**Key Functions:**

* `find_K(probabilities, skewness_log, source='scipy')`:
    Finds the K values (frequency factors) corresponding 
        to given probabilities and skewness (logarithm of the skewness values).

* `calc_x_logpearson3(input_array, return_periods=[5], source='scipy', display_stat=False)`:
    Calculates the value of x (e.g., flood discharge) for given return periods 
        using the Log-Pearson Type III distribution.

* `freq_logpearson3(
        dataframe, target_column, return_periods, display_stat=False, 
        source='scipy', out_column_name='Log Pearson III', out_index_name='Kala Ulang')`:
    Performs frequency analysis using the Log-Pearson Type III method 
        on a pandas DataFrame.

* `calc_prob(k, skew_log, source='scipy')`:
    Calculates the probability value for a given K value and skew_log (logarithm of skewness).

**Deprecated Functions:**

* `calc_x_lp3`: Deprecated alias for `calc_x_logpearson3`.

manual:
    https://gist.github.com/taruma/60725ffca91dc6e741daee9a738a978b
"""

import numpy as np
import pandas as pd
from scipy import stats, interpolate
from hidrokit.contrib.taruma.utils import handle_deprecated_params, deprecated

# tabel dari Soewarno, hal. 219
# lampiran tabel III-3, Nilai k Distribusi Pearson tipe III
# dan Log Pearson ti

# kode: SW

# fmt: off
_DATA_SW = np.array([
    [-0.360, 0.420, 1.180, 2.278, 3.152, 4.051, 4.970, 7.250],
    [-0.360, 0.518, 1.250, 2.262, 3.048, 3.845, 4.652, 6.600],
    [-0.330, 0.574, 1.284, 2.240, 2.970, 3.705, 4.444, 6.200],
    [-0.307, 0.609, 1.302, 2.219, 2.912, 3.605, 4.298, 5.910],
    [-0.282, 0.643, 1.318, 2.193, 2.848, 3.499, 4.147, 5.660],
    [-0.254, 0.675, 1.329, 2.163, 2.780, 3.388, 3.990, 5.390],
    [-0.225, 0.705, 1.337, 2.128, 2.706, 3.271, 3.828, 5.110],
    [-0.195, 0.732, 1.340, 2.087, 2.626, 3.149, 3.661, 4.820],
    [-0.164, 0.758, 1.340, 2.043, 2.542, 3.022, 3.489, 4.540],
    [-0.148, 0.769, 1.339, 2.018, 2.498, 2.957, 3.401, 4.395],
    [-0.132, 0.780, 1.336, 1.998, 2.453, 2.891, 3.312, 4.250],
    [-0.116, 0.790, 1.333, 1.967, 2.407, 2.824, 3.223, 4.105],
    [0.099, 0.800, 1.328, 1.939, 2.359, 2.755, 3.132, 3.960],
    [-0.083, 0.808, 1.323, 1.910, 2.311, 2.686, 3.041, 3.815],
    [-0.066, 0.816, 1.317, 1.880, 2.261, 2.615, 2.949, 3.670],
    [-0.050, 0.824, 1.309, 1.849, 2.211, 2.544, 2.856, 3.525],
    [-0.033, 0.830, 1.301, 1.818, 2.159, 2.472, 2.763, 3.380],
    [-0.017, 0.836, 1.292, 1.785, 2.107, 2.400, 2.670, 3.235],
    [0.000, 0.842, 1.282, 1.751, 2.054, 2.326, 2.576, 3.090],
    [0.017, 0.836, 1.270, 1.761, 2.000, 2.252, 2.482, 3.950],
    [0.033, 0.850, 1.258, 1.680, 1.945, 2.178, 2.388, 2.810],
    [0.050, 0.853, 1.245, 1.643, 1.890, 2.104, 2.294, 2.675],
    [0.066, 0.855, 1.231, 1.606, 1.834, 2.029, 2.201, 2.540],
    [0.083, 0.856, 1.216, 1.567, 1.777, 1.955, 2.108, 2.400],
    [0.099, 0.857, 1.200, 1.528, 1.720, 1.880, 2.016, 2.275],
    [0.116, 0.857, 1.183, 1.488, 1.663, 1.806, 1.926, 2.150],
    [0.132, 0.856, 1.166, 1.448, 1.606, 1.733, 1.837, 2.035],
    [0.148, 0.854, 1.147, 1.407, 1.549, 1.660, 1.749, 1.910],
    [0.164, 0.852, 1.128, 1.366, 1.492, 1.588, 1.664, 1.800],
    [0.195, 0.844, 1.086, 1.282, 1.379, 1.449, 1.501, 1.625],
    [0.225, 0.832, 1.041, 1.198, 1.270, 1.318, 1.351, 1.465],
    [0.254, 0.817, 0.994, 1.116, 1.166, 1.197, 1.216, 1.280],
    [0.282, 0.799, 0.945, 1.035, 1.069, 1.087, 1.097, 1.130],
    [0.307, 0.777, 0.895, 0.959, 0.980, 0.990, 1.995, 1.000],
    [0.330, 0.752, 0.844, 0.888, 0.900, 0.905, 0.907, 0.910],
    [0.360, 0.711, 0.771, 0.793, 0.798, 0.799, 0.800, 0.802],
    [0.396, 0.636, 0.660, 0.666, 0.666, 0.667, 0.667, 0.668]]
)

_INDEX_SW = [
    3, 2.5, 2.2, 2, 1.8, 1.6, 1.4, 1.2, 1,
    0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1, 0,
    -0.1, -0.2, -0.3, -0.4, -0.5, -0.6, -0.7, -0.8, -0.9, -1,
    -1.2, -1.4, -1.6, -1.8, -2., -2.2, -2.5, -3.
]

_COL_SW = [0.5, 0.2, 0.1, 0.04, 0.02, 0.01, 0.005, 0.001]

t_pearson3_sw = pd.DataFrame(data=_DATA_SW, index=_INDEX_SW, columns=_COL_SW)

# Tabel dari Soetopo hal. 105
# Tabel Distribusi Pearson Type III (nilai K)

# KODE: ST

_DATA_ST = [
    [-4.051, -2.003, -1.180, -0.420, 0.396, 0.636, 0.660, 0.666, 0.666, 0.667, 0.667, 0.667],
    [-4.013, -2.007, -1.195, -0.440, 0.390, 0.651, 0.681, 0.688, 0.689, 0.690, 0.690, 0.690],
    [-3.973, -2.010, -1.210, -0.460, 0.384, 0.666, 0.702, 0.712, 0.714, 0.714, 0.714, 0.714],
    [-3.932, -2.012, -1.224, -0.479, 0.376, 0.681, 0.724, 0.738, 0.740, 0.740, 0.741, 0.741],
    [-3.889, -2.013, -1.238, -0.499, 0.369, 0.696, 0.747, 0.765, 0.768, 0.769, 0.769, 0.769],
    [-3.845, -2.012, -1.250, -0.518, 0.360, 0.711, 0.771, 0.793, 0.798, 0.799, 0.800, 0.800],
    [-3.800, -2.011, -1.262, -0.537, 0.351, 0.725, 0.795, 0.823, 0.830, 0.832, 0.833, 0.833],
    [-3.753, -2.009, -1.274, -0.555, 0.341, 0.739, 0.819, 0.855, 0.864, 0.867, 0.869, 0.869],
    [-3.705, -2.006, -1.284, -0.574, 0.330, 0.752, 0.844, 0.888, 0.900, 0.905, 0.907, 0.909],
    [-3.656, -2.001, -1.294, -0.592, 0.319, 0.765, 0.869, 0.923, 0.939, 0.946, 0.949, 0.952],
    [-3.605, -1.996, -1.303, -0.609, 0.307, 0.777, 0.895, 0.959, 0.980, 0.990, 0.995, 0.999],
    [-3.553, -1.989, -1.311, -0.627, 0.294, 0.788, 0.920, 0.997, 1.023, 1.037, 1.044, 1.051],
    [-3.499, -1.981, -1.318, -0.643, 0.282, 0.799, 0.945, 1.035, 1.069, 1.087, 1.097, 1.107],
    [-3.444, -1.972, -1.324, -0.660, 0.268, 0.808, 0.970, 1.075, 1.116, 1.140, 1.155, 1.170],
    [-3.388, -1.962, -1.329, -0.675, 0.254, 0.817, 0.994, 1.116, 1.166, 1.197, 1.216, 1.238],
    [-3.330, -1.951, -1.333, -0.691, 0.240, 0.825, 1.018, 1.157, 1.217, 1.256, 1.282, 1.313],
    [-3.271, -1.938, -1.337, -0.705, 0.225, 0.832, 1.041, 1.198, 1.270, 1.318, 1.351, 1.394],
    [-3.211, -1.925, -1.339, -0.719, 0.210, 0.838, 1.064, 1.240, 1.324, 1.383, 1.424, 1.482],
    [-3.149, -1.910, -1.340, -0.733, 0.195, 0.844, 1.086, 1.282, 1.379, 1.449, 1.501, 1.577],
    [-3.087, -1.894, -1.341, -0.745, 0.180, 0.848, 1.107, 1.324, 1.435, 1.518, 1.581, 1.678],
    [-3.023, -1.877, -1.340, -0.758, 0.164, 0.852, 1.128, 1.366, 1.492, 1.588, 1.664, 1.786],
    [-2.957, -1.859, -1.339, -0.769, 0.148, 0.854, 1.147, 1.407, 1.549, 1.660, 1.749, 1.899],
    [-2.891, -1.839, -1.336, -0.780, 0.132, 0.856, 1.166, 1.448, 1.606, 1.733, 1.837, 2.017],
    [-2.824, -1.819, -1.333, -0.790, 0.116, 0.857, 1.183, 1.489, 1.663, 1.806, 1.926, 2.141],
    [-2.755, -1.797, -1.329, -0.800, 0.099, 0.857, 1.200, 1.528, 1.720, 1.880, 2.016, 2.268],
    [-2.686, -1.774, -1.323, -0.808, 0.083, 0.857, 1.216, 1.567, 1.777, 1.955, 2.108, 2.399],
    [-2.615, -1.750, -1.317, -0.816, 0.067, 0.855, 1.231, 1.606, 1.834, 2.029, 2.201, 2.533],
    [-2.544, -1.726, -1.309, -0.824, 0.050, 0.853, 1.245, 1.643, 1.890, 2.104, 2.294, 2.669],
    [-2.472, -1.700, -1.301, -0.830, 0.033, 0.850, 1.258, 1.680, 1.945, 2.178, 2.388, 2.808],
    [-2.400, -1.673, -1.292, -0.836, 0.017, 0.846, 1.270, 1.716, 2.000, 2.253, 2.482, 2.948],
    [-2.326, -1.645, -1.282, -0.842, 0.000, 0.842, 1.282, 1.751, 2.054, 2.326, 2.576, 3.090],
    [-2.253, -1.616, -1.270, -0.846, -0.017, 0.836, 1.292, 1.785, 2.107, 2.400, 2.670, 3.233],
    [-2.178, -1.586, -1.258, -0.850, -0.033, 0.830, 1.301, 1.818, 2.159, 2.472, 2.763, 3.377],
    [-2.104, -1.555, -1.245, -0.853, -0.050, 0.824, 1.309, 1.849, 2.211, 2.544, 2.856, 3.521],
    [-2.029, -1.524, -1.231, -0.855, -0.067, 0.816, 1.317, 1.880, 2.261, 2.615, 2.949, 3.666],
    [-1.955, -1.491, -1.216, -0.857, -0.083, 0.808, 1.323, 1.910, 2.311, 2.686, 3.041, 3.811],
    [-1.880, -1.458, -1.200, -0.857, -0.099, 0.800, 1.329, 1.939, 2.359, 2.755, 3.132, 3.956],
    [-1.806, -1.423, -1.183, -0.857, -0.116, 0.790, 1.333, 1.967, 2.407, 2.824, 3.223, 4.100],
    [-1.733, -1.389, -1.166, -0.856, -0.132, 0.780, 1.336, 1.993, 2.453, 2.891, 3.312, 4.244],
    [-1.660, -1.353, -1.147, -0.854, -0.148, 0.769, 1.339, 2.018, 2.498, 2.957, 3.401, 4.388],
    [-1.588, -1.317, -1.128, -0.852, -0.164, 0.758, 1.340, 2.043, 2.542, 3.023, 3.489, 4.531],
    [-1.518, -1.280, -1.107, -0.848, -0.180, 0.745, 1.341, 2.066, 2.585, 3.087, 3.575, 4.673],
    [-1.449, -1.243, -1.086, -0.844, -0.195, 0.733, 1.340, 2.088, 2.626, 3.149, 3.661, 4.815],
    [-1.383, -1.206, -1.064, -0.838, -0.210, 0.719, 1.339, 2.108, 2.667, 3.211, 3.745, 4.955],
    [-1.318, -1.168, -1.041, -0.832, -0.225, 0.705, 1.337, 2.128, 2.706, 3.271, 3.828, 5.095],
    [-1.256, -1.131, -1.018, -0.825, -0.240, 0.691, 1.333, 2.146, 2.743, 3.330, 3.910, 5.234],
    [-1.197, -1.093, -0.994, -0.817, -0.254, 0.675, 1.329, 2.163, 2.780, 3.388, 3.990, 5.371],
    [-1.140, -1.056, -0.970, -0.808, -0.268, 0.660, 1.324, 2.179, 2.815, 3.444, 4.069, 5.507],
    [-1.087, -1.020, -0.945, -0.799, -0.282, 0.643, 1.318, 2.193, 2.848, 3.499, 4.147, 5.642],
    [-1.037, -0.984, -0.920, -0.788, -0.294, 0.627, 1.311, 2.207, 2.881, 3.553, 4.223, 5.775],
    [-0.990, -0.949, -0.895, -0.777, -0.307, 0.609, 1.303, 2.219, 2.912, 3.605, 4.298, 5.908],
    [-0.946, -0.915, -0.869, -0.765, -0.319, 0.592, 1.294, 2.230, 2.942, 3.656, 4.372, 6.039],
    [-0.905, -0.882, -0.844, -0.752, -0.330, 0.574, 1.284, 2.240, 2.970, 3.705, 4.444, 6.168],
    [-0.867, -0.850, -0.819, -0.739, -0.341, 0.555, 1.274, 2.248, 2.997, 3.753, 4.515, 6.296],
    [-0.832, -0.819, -0.795, -0.725, -0.351, 0.537, 1.262, 2.256, 3.023, 3.800, 4.584, 6.423],
    [-0.799, -0.790, -0.771, -0.711, -0.360, 0.518, 1.250, 2.262, 3.048, 3.845, 4.652, 6.548],
    [-0.769, -0.762, -0.747, -0.696, -0.369, 0.499, 1.238, 2.267, 3.071, 3.889, 4.718, 6.672],
    [-0.740, -0.736, -0.724, -0.681, -0.376, 0.479, 1.224, 2.272, 3.093, 3.932, 4.783, 6.794],
    [-0.714, -0.711, -0.702, -0.666, -0.384, 0.460, 1.210, 2.275, 3.114, 3.973, 4.847, 6.915],
    [-0.690, -0.688, -0.681, -0.651, -0.390, 0.440, 1.195, 2.277, 3.134, 4.013, 4.909, 7.034],
    [-0.667, -0.665, -0.660, -0.636, -0.396, 0.420, 1.180, 2.278, 3.152, 4.051, 4.970, 7.152]
]

_INDEX_ST = np.arange(-30, 31, 1)/10

_COL_ST = np.array([99, 95, 90, 80, 50, 20, 10, 4, 2, 1, 0.5, 0.1])/100

t_pearson3_st = pd.DataFrame(data=_DATA_ST, index=_INDEX_ST, columns=_COL_ST)

# Dari buku Limantara hal. 107-109
# Tabel Distribsi log Pearson Tipe III Nilai G
# Untuk Cs Positif & Negatif

# KODE: LM

_DATA_LM = [
    [-0.667, -0.665, -0.660, -0.636, -0.396, 0.420, 1.180, 2.278, 3.152, 4.061, 4.970],
    [-0.690, -0.688, -0.681, -0.651, -0.390, 0.440, 1.196, 2.277, 3.134, 4.013, 4.909],
    [-0.714, -0.711, -0.702, -0.666, -0.384, 0.460, 1.210, 2.275, 3.114, 3.973, 4.847],
    [-0.740, -0.736, -0.724, -0.681, -0.376, 0.479, 1.224, 2.272, 3.097, 3.932, 4.783],
    [-0.769, -0.762, -0.747, -0.695, -0.368, 0.499, 1.238, 2.267, 3.071, 3.889, 4.718],
    [-0.799, -0.790, -0.771, -0.711, -0.360, 0.518, 1.250, 2.262, 3.048, 3.845, 4.652],
    [-0.832, -0.819, -0.795, -0.725, -0.351, 0.537, 1.262, 2.256, 3.029, 3.800, 4.584],
    [-0.867, -0.850, -0.819, -0.739, -0.341, 0.555, 1.274, 2.248, 2.997, 3.753, 4.515],
    [-0.905, -0.882, -0.844, -0.752, -0.330, 0.574, 1.284, 2.240, 2.970, 3.705, 4.454],
    [-0.946, -0.914, -0.869, -0.765, -0.319, 0.592, 1.294, 2.230, 2.942, 3.656, 4.372],
    [-0.990, -0.949, -0.896, -0.777, -0.307, 0.609, 1.302, 2.219, 2.912, 3.605, 4.298],
    [-1.037, -0.984, -0.920, -0.788, -0.294, 0.627, 1.310, 2.207, 2.881, 3.553, 4.223],
    [-1.087, -1.020, -0.945, -0.799, -0.282, 0.643, 1.318, 2.193, 2.848, 3.499, 4.147],
    [-1.140, -1.056, -0.970, -0.808, -0.268, 0.660, 1.324, 2.179, 2.815, 3.444, 4.069],
    [-1.197, -1.093, -0.994, -0.817, -0.254, 0.675, 1.329, 2.163, 2.780, 3.388, 3.990],
    [-1.256, -1.131, -1.018, -0.825, -0.240, 0.690, 1.333, 2.146, 2.745, 3.330, 3.910],
    [-1.318, -1.163, -1.041, -0.832, -0.225, 0.705, 1.337, 2.128, 2.706, 3.271, 3.828],
    [-1.388, -1.206, -1.064, -0.838, -0.210, 0.719, 1.339, 2.108, 2.666, 3.211, 3.745],
    [-1.449, -1.243, -1.086, -0.844, -0.195, 0.732, 1.340, 2.087, 2.626, 3.149, 3.661],
    [-1.518, -1.280, -1.107, -0.848, -0.180, 0.745, 1.341, 2.066, 2.585, 3.087, 3.575],
    [-1.588, -1.317, -1.128, -0.852, -0.164, 0.758, 1.340, 2.043, 2.542, 3.022, 3.489],
    [-1.660, -1.353, -1.147, -0.854, -0.148, 0.769, 1.339, 2.018, 2.498, 2.967, 3.401],
    [-1.733, -1.388, -1.166, -0.856, -0.132, 0.780, 1.336, 1.993, 2.453, 2.891, 3.312],
    [-1.806, -1.423, -1.183, -0.857, -0.116, 0.790, 1.333, 1.967, 2.407, 2.824, 3.223],
    [-1.880, -1.458, -1.200, -0.857, -0.099, 0.800, 1.328, 1.939, 2.359, 2.755, 3.123],
    [-1.965, -1.491, -1.216, -0.856, -0.083, 0.808, 1.323, 1.910, 2.311, 2.686, 3.041],
    [-2.029, -1.524, -1.231, -0.855, -0.066, 0.816, 1.317, 1.880, 2.261, 2.615, 2.949],
    [-2.104, -1.555, -1.245, -0.853, -0.050, 0.824, 1.309, 1.849, 2.211, 2.544, 2.856],
    [-2.175, -1.586, -1.258, -0.850, -0.033, 0.830, 1.301, 1.818, 2.159, 2.472, 2.763],
    [-2.225, -1.616, -1.270, -0.846, -0.017, 0.836, 1.292, 1.785, 2.107, 2.400, 2.670],
    [-2.326, -1.645, -1.282, -0.842, 0.000, 0.842, 1.282, 1.751, 2.064, 2.064, 2.576],
    [-2.400, -1.673, -1.292, -0.836, 0.017, 0.846, 1.270, 1.716, 2.000, 2.252, 2.482],
    [-2.472, -1.700, -1.301, -0.830, 0.033, 0.850, 1.258, 1.680, 1.945, 2.178, 2.388],
    [-2.544, -1.762, -1.309, -0.824, 0.050, 0.853, 1.245, 0.163, 1.890, 2.104, 2.294],
    [-2.615, -1.750, -1.317, -0.816, 0.066, 0.855, 1.231, 1.606, 1.834, 2.029, 2.201],
    [-2.686, -1.774, -1.323, -0.808, 0.083, 0.856, 1.216, 1.567, 1.777, 1.955, 2.108],
    [-2.755, -1.797, -1.328, -0.800, 0.099, 0.857, 1.200, 1.528, 1.720, 1.880, 2.016],
    [-2.824, -1.819, -1.333, -0.790, 0.116, 0.857, 1.183, 1.488, 1.633, 1.800, 1.936],
    [-2.891, -1.839, -1.336, -0.780, 0.132, 0.856, 1.166, 1.484, 1.608, 1.733, 1.837],
    [-2.957, -1.858, -1.339, -0.769, 0.148, 0.854, 1.147, 1.407, 1.549, 1.660, 1.749],
    [-3.022, -1.877, -1.340, -0.758, 0.164, 0.852, 1.108, 1.366, 1.492, 1.588, 1.664],
    [-3.087, -1.894, -1.341, -0.745, 0.180, 0.848, 1.107, 1.324, 1.435, 1.518, 1.581],
    [-3.149, -1.910, -1.340, -0.732, 0.195, 0.844, 1.086, 1.282, 1.379, 1.449, 1.501],
    [-3.211, -1.925, -1.339, -0.719, 0.210, 0.838, 1.064, 1.240, 1.324, 1.383, 1.424],
    [-3.271, -1.938, -1.337, -0.705, 0.225, 0.832, 1.041, 1.196, 1.270, 1.316, 1.351],
    [-3.330, -1.961, -1.333, -0.690, 0.240, 0.825, 1.018, 1.157, 1.217, 1.256, 1.282],
    [-3.388, -1.962, -1.329, -0.675, 0.254, 0.817, 0.994, 1.116, 1.168, 1.197, 1.216],
    [-3.444, -1.972, -1.324, -0.660, 0.268, 0.808, 0.970, 1.075, 1.116, 1.140, 1.155],
    [-3.499, -1.981, -1.318, -0.643, 0.282, 0.799, 0.945, 1.035, 1.069, 1.087, 1.097],
    [-3.533, -1.989, -1.310, -0.627, 0.294, 0.788, 0.920, 0.996, 1.023, 1.037, 1.044],
    [-3.605, -1.996, -1.302, -0.609, 0.307, 0.777, 0.895, 0.969, 0.980, 0.990, 0.995],
    [-3.656, -2.001, -1.294, -0.592, 0.319, 0.765, 0.869, 0.923, 0.939, 0.346, 0.949],
    [-3.705, -2.006, -1.284, -0.574, 0.330, 0.732, 0.849, 0.888, 0.900, 0.905, 0.907],
    [-3.753, -2.009, -1.274, -0.555, 0.341, 0.739, 0.819, 0.855, 0.864, 0.867, 0.869],
    [-3.800, -2.011, -1.262, -0.537, 0.351, 0.725, 0.795, 0.823, 0.830, 0.832, 0.833],
    [-3.845, -2.012, -1.250, -0.518, 0.360, 0.711, 0.771, 0.793, 0.796, 0.799, 0.800],
    [-3.889, -2.013, -1.238, -0.499, 0.368, 0.696, 0.747, 0.764, 0.767, 0.769, 0.769],
    [-3.932, -2.011, -1.224, -0.479, 0.376, 0.681, 0.724, 0.738, 0.740, 0.740, 0.741],
    [-3.973, -2.010, -1.210, -0.460, 0.384, 0.666, 0.702, 0.712, 0.714, 0.734, 0.714],
    [-4.013, -2.007, -1.195, -0.440, 0.330, 0.651, 0.681, 0.683, 0.689, 0.690, 0.690],
    [-4.051, -2.003, -1.180, -0.420, 0.390, 0.636, 0.660, 0.666, 0.666, 0.667, 0.667]
]

_INDEX_LM = np.arange(30, -31, -1) / 10

_COL_LM =  np.array([99, 95, 90, 80, 50, 20, 10, 4, 2, 1, 0.5])/100

t_pearson3_lm = pd.DataFrame(data=_DATA_LM, index=_INDEX_LM, columns=_COL_LM)

# fmt: on

# KODE FUNGSI INTERPOLASI DARI TABEL


def _func_interp_bivariate(df):
    "Membuat fungsi dari tabel untuk interpolasi bilinear"
    table = df[df.columns.sort_values()].sort_index().copy()

    x = table.index
    y = table.columns
    z = table.to_numpy()

    # penggunaan kx=1, ky=1 untuk interpolasi linear antara 2 titik
    # tidak menggunakan (cubic) spline interpolation
    return interpolate.RectBivariateSpline(x, y, z, kx=1, ky=1)


def _as_value(x):
    x = np.around(x, 4)
    return x.flatten() if x.size > 1 else x.item()


# pylint: disable=invalid-name


def find_K(probabilities=None, skewness_log=None, source="scipy", **kwargs):
    """
    Find the K values corresponding to given probabilities and skewness.

    Parameters:
    - probabilities (array-like): An array-like object containing the probabilities.
    - skewness_log (array-like): An array-like object containing the logarithm of skewness values.
    - source (str): The source of the K values.
        Options are 'scipy', 'soetopo', 'soewarno', 'limantara'.
        Default is 'scipy'.

    Returns:
    - k_values (array-like):
        An array-like object containing the K values corresponding
        to the given probabilities and skewness.

    Raises:
    - ValueError: If the specified source is not found.

    """
    # deprecated parameters
    probabilities = (
        handle_deprecated_params(kwargs, "prob", "probabilities") or probabilities
    )
    skewness_log = (
        handle_deprecated_params(kwargs, "skew", "skewness_log") or skewness_log
    )

    probabilities = np.array(probabilities)
    if source.lower() == "scipy":
        # ref: https://github.com/hidrokit/hidrokit/discussions/156
        k_values = np.around(stats.pearson3.ppf(1 - probabilities, skewness_log), 4)
    elif source.lower() == "soetopo":
        func_pearson3_st = _func_interp_bivariate(t_pearson3_st)
        k_values = _as_value(func_pearson3_st(skewness_log, probabilities, grid=False))
    elif source.lower() == "soewarno":
        func_pearson3_sw = _func_interp_bivariate(t_pearson3_sw)
        k_values = _as_value(func_pearson3_sw(skewness_log, probabilities, grid=False))
    elif source.lower() == "limantara":
        func_pearson3_lm = _func_interp_bivariate(t_pearson3_lm)
        k_values = _as_value(func_pearson3_lm(skewness_log, probabilities, grid=False))
    else:
        raise ValueError(f"source '{source}' not found")

    return k_values


def calc_x_logpearson3(
    input_array=None, return_periods=None, source="scipy", display_stat=False
):
    """
    Calculate the value of x using the Log-Pearson Type III distribution.

    Parameters:
    - input_array (array-like): The input array of values.
    - return_periods (list): The list of return periods. Default is [5].
    - source (str): The source of the calculation method. Default is "scipy".
    - display_stat (bool): Whether to display the calculated statistics. Default is False.

    Returns:
    - val_x (float): The calculated value of x.

    """
    return_periods = [5] if return_periods is None else return_periods

    y = np.log10(input_array)
    y_mean = np.mean(y)
    y_std = np.std(y, ddof=1)
    y_skew = stats.skew(y, bias=False)

    prob = 1 / np.array(return_periods)
    k = find_K(prob, y_skew, source=source)

    if display_stat:
        print(f"y_mean = {y_mean:.5f}")
        print(f"y_std = {y_std:.5f}")
        print(f"y_skew = {y_skew:.5f}")
        print(f"k = {k}")

    val_y = y_mean + k * y_std
    val_x = np.power(10, val_y)
    return val_x


@deprecated("calc_x_logpearson3")
def calc_x_lp3(x, return_period=None, source="scipy", show_stat=False):
    """Calculate the value of x using the Log-Pearson Type III distribution."""
    return_period = [5] if return_period is None else return_period
    return calc_x_logpearson3(
        input_array=x,
        return_periods=return_period,
        source=source,
        display_stat=show_stat,
    )


# pylint: disable=too-many-arguments
def freq_logpearson3(
    dataframe=None,
    target_column=None,
    return_periods=None,
    display_stat=False,
    source="scipy",
    out_column_name="Log Pearson III",
    out_index_name="Kala Ulang",
    **kwargs,
):
    """
    Calculate the frequency analysis using the Log Pearson III method.

    Parameters:
    - dataframe: pandas DataFrame, optional (default=None)
        The input data frame containing the target column.
    - target_column: str, optional (default=None)
        The name of the target column in the data frame.
    - return_periods: list, optional (default=[2, 5, 10, 20, 25, 50, 100])
        The return periods for which to calculate the frequency analysis.
    - display_stat: bool, optional (default=False)
        Whether to display the statistical parameters of the Log Pearson III distribution.
    - source: str, optional (default="scipy")
        The source of the Log Pearson III distribution parameters.
    - out_column_name: str, optional (default="Log Pearson III")
        The name of the output column in the result DataFrame.
    - out_index_name: str, optional (default="Kala Ulang")
        The name of the output index in the result DataFrame.
    - **kwargs: dict, optional
        Additional deprecated parameters.

    Returns:
    - result: pandas DataFrame
        The result DataFrame containing the frequency analysis for the specified return periods.
    """

    # deprecated parameters
    dataframe = handle_deprecated_params(kwargs, "df", "dataframe") or dataframe
    target_column = (
        handle_deprecated_params(kwargs, "col", "target_column") or target_column
    )
    return_periods = (
        handle_deprecated_params(kwargs, "return_period", "return_periods")
        or return_periods
    )
    display_stat = (
        handle_deprecated_params(kwargs, "show_stat", "display_stat") or display_stat
    )
    out_column_name = (
        handle_deprecated_params(kwargs, "col_name", "out_column_name")
        or out_column_name
    )
    out_index_name = (
        handle_deprecated_params(kwargs, "index_name", "out_index_name")
        or out_index_name
    )

    return_periods = (
        [2, 5, 10, 20, 25, 50, 100] if return_periods is None else return_periods
    )

    target_column = dataframe.columns[0] if target_column is None else target_column

    x = dataframe[target_column].copy()

    arr = calc_x_logpearson3(
        x, return_periods=return_periods, display_stat=display_stat, source=source
    )

    result = pd.DataFrame(data=arr, index=return_periods, columns=[out_column_name])

    result.index.name = out_index_name
    return result


dict_table_source = {
    "soewarno": t_pearson3_sw,
    "soetopo": t_pearson3_st,
    "limantara": t_pearson3_lm,
}


def _find_prob_in_table(k, skew_log, table):
    func_table = _func_interp_bivariate(table)
    y = table.columns
    x = func_table(skew_log, y, grid=False)
    func_prob = interpolate.interp1d(x, y, kind="linear")
    return _as_value(func_prob(k))


def _calc_prob_in_table(k, skew_log, source="soewarno"):
    if source.lower() in dict_table_source:
        return 1 - _find_prob_in_table(k, skew_log, dict_table_source[source.lower()])
    return None


def calc_prob(k, skew_log, source="scipy"):
    """
    Calculate the probability value for a given value of k and skew_log.

    Parameters:
    k (float): The value of k.
    skew_log (float): The skew_log value.
    source (str, optional): The source of the probability calculation. Defaults to "scipy".

    Returns:
    float: The calculated probability value.

    Raises:
    ValueError: If the source is not found in the available sources.

    """
    if source.lower() == "scipy":
        prob_value = stats.pearson3.cdf(k, skew_log)
    elif source.lower() in dict_table_source:
        prob_value = _calc_prob_in_table(k, skew_log, source.lower())
    else:
        raise ValueError(f"source '{source}' not found")

    return prob_value
