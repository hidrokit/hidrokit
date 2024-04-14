"""
hk106: evapotranspiration.py

This module provides functions for calculating evapotranspiration (ETo) 
    using different methods: Blaney Criddle, Radiation, and Penman.

Functions:
    - ETo_BlaneyCriddle(df, temp_col, lat, as_df=True, report="ETo"): 
        Calculates ETo using the Blaney Criddle method.
    - ETo_Radiation(df, temp_col, sun_col, lat, as_df=True, report="ETo"): 
        Calculates ETo using the Radiation method.
    - ETo_Penman(df, temp_col, humid_col, wind_col, sun_col, lat, as_df=True, report="ETo"): 
        Calculates ETo using the Penman method.

manual:
    https://gist.github.com/taruma/7f81cf0fea5250cfe47942b4e16a8a65
"""

import numpy as np
import pandas as pd
from hidrokit.contrib.taruma.utils import handle_deprecated_params, deprecated

# pylint: disable=invalid-name, too-many-arguments, too-many-locals, too-many-statements

t_rel_P_LL = pd.DataFrame(
    {
        "5 U": [0.27] * 3 + [0.28] * 6 + [0.27] * 3,
        "2.5 U": [0.27] * 3 + [0.28] * 6 + [0.27] * 3,
        "0": [0.27] * 12,
        "2.5 S": [0.28] * 12,
        "5 S": [0.28] * 12,
        "7.5 S": [0.28] * 4 + [0.27] * 4 + [0.28] * 3 + [0.29] * 1,
        "10 S": [0.29]
        + [0.28] * 2
        + [0.27]
        + [0.26] * 4
        + [0.27]
        + [0.28] * 2
        + [0.29],
    },
    index=range(1, 13),
)

t_cor_C_BC = pd.DataFrame(
    {"C": [0.8, 0.8, 0.75, 0.7, 0.7, 0.7, 0.7, 0.75, 0.8, 0.8, 0.8, 0.8]},
    index=range(1, 13),
)

t_rel_T_W = pd.DataFrame(
    {"suhu": np.arange(24.0, 30, 0.2), "W": np.arange(0.735, 0.794, 0.002)}
)

t_cor_C_RAD = pd.DataFrame(
    {"C": [0.8] * 2 + [0.75] * 5 + [0.8] * 5}, index=range(1, 13)
)

_data = [
    13.0,
    14.3,
    14.7,
    15.0,
    15.3,
    15.5,
    15.8,
    16.1,
    16.1,
    14.0,
    15.0,
    15.3,
    15.5,
    15.7,
    15.8,
    16.0,
    16.1,
    16.0,
    15.0,
    15.5,
    15.6,
    15.7,
    15.7,
    15.6,
    15.6,
    15.1,
    15.3,
    15.1,
    15.5,
    15.3,
    15.3,
    15.1,
    14.9,
    14.7,
    14.1,
    14.0,
    15.3,
    14.9,
    14.6,
    14.4,
    14.1,
    13.8,
    13.4,
    13.1,
    12.6,
    15.0,
    14.4,
    14.2,
    13.9,
    13.9,
    13.2,
    12.8,
    12.4,
    12.6,
    15.1,
    14.6,
    14.3,
    14.1,
    14.1,
    13.4,
    13.1,
    12.7,
    11.8,
    15.3,
    15.1,
    14.9,
    14.8,
    14.8,
    14.3,
    14.0,
    13.7,
    12.2,
    15.1,
    15.3,
    15.3,
    15.3,
    15.3,
    15.1,
    15.0,
    14.9,
    13.1,
    15.7,
    15.1,
    15.3,
    15.4,
    15.4,
    15.6,
    15.7,
    15.8,
    14.6,
    14.8,
    14.5,
    14.8,
    15.1,
    15.1,
    15.5,
    15.8,
    16.0,
    15.6,
    14.6,
    14.1,
    14.4,
    14.8,
    14.8,
    15.4,
    15.7,
    16.0,
    16.0,
]
_data = np.array(_data).reshape((12, 9)).T
t_val_Rg = pd.DataFrame(
    _data,
    columns=range(1, 13),
    index=["5 LU", "4 LU", "2 LU", "0", "2 LS", "4 LS", "6 LS", "8 LS", "10 LS"],
).T

t_cor_C_PEN = pd.DataFrame(
    {
        "C": [1.1] * 3 + [0.9] * 4 + [1.1] * 5,
    },
    index=range(1, 13),
)

t_rel_T_PEN = pd.DataFrame(
    {
        "suhu": np.arange(24.0, 29.1, 0.2),
        "e_mbar": [
            29.85,
            30.21,
            30.57,
            30.94,
            31.31,
            31.69,
            32.06,
            32.45,
            32.83,
            32.22,
            33.62,
            34.02,
            34.42,
            34.83,
            35.25,
            35.66,
            36.09,
            36.50,
            36.94,
            37.37,
            37.81,
            38.25,
            38.70,
            39.14,
            39.61,
            40.06,
        ],
        "w": np.arange(0.735, 0.786, 0.002),
        "f_t": [
            15.40,
            15.45,
            15.50,
            15.55,
            15.60,
            15.65,
            15.70,
            15.75,
            15.80,
            15.85,
            15.90,
            15.94,
            15.98,
            16.02,
            16.06,
            16.10,
            16.14,
            16.18,
            16.22,
            16.26,
            16.30,
            16.34,
            16.38,
            16.42,
            16.46,
            16.5,
        ],
    }
)


def __lat_to_num(lat):
    num, lat = lat.split(" ")
    num = float(num)
    num = -num if lat.lower() == "lu" else num
    return num


# Blaney Criddle


def _BC_ETo(c, ETo_x):
    return c * ETo_x


def _BC_ETo_x(P, temp):
    return P * (0.457 * temp + 8.13)


def _BC_find_P(latitude, month, table=t_rel_P_LL):
    m = table.loc[month].values
    x = [-5, -2.5, 0, 2.5, 5, 7.5, 10]
    return np.interp(__lat_to_num(latitude), x, m)


def _BC_find_C(month, table=t_cor_C_BC, col="C"):
    return table.loc[month, col]


def eto_blaney_criddle(
    dataframe,
    temperature_column,
    latitude,
    return_as_dataframe=True,
    report_type="ETo",
    **kwargs
):
    """
    Calculate evapotranspiration (ETo) using the Blaney-Criddle method.

    Parameters:
    - dataframe (pandas.DataFrame): The input dataframe containing the temperature data.
    - temperature_column (str): The name of the column in the dataframe
        that contains the temperature data.
    - latitude (str): The latitude of the location.
    - return_as_dataframe (bool, optional): Whether to return the results as a dataframe.
        Default is True.
    - report_type (str, optional): The type of report to generate.
        Valid values are "ETo" (default), "full", or "eto".
    - **kwargs: Additional keyword arguments for deprecated parameters.
        - df (pandas.DataFrame): Deprecated. Use dataframe instead.
        - temp_col (str): Deprecated. Use temperature_column instead.
        - lat (str): Deprecated. Use latitude instead.
        - as_df (bool): Deprecated. Use return_as_dataframe instead.
        - report (str): Deprecated. Use report_type instead.

    Returns:
    - If return_as_dataframe is True:
        - pandas.DataFrame: A dataframe containing the calculated ETo values
            and other relevant information.
    - If return_as_dataframe is False:
        - numpy.ndarray: An array containing the calculated ETo values.

    Note:
    - The Blaney-Criddle method estimates ETo based on temperature and latitude.
    - The function supports deprecated parameters for backward compatibility.
    """

    # handle deprecated params
    dataframe = handle_deprecated_params(kwargs, "df", "dataframe") or dataframe
    temperature_column = (
        handle_deprecated_params(kwargs, "temp_col", "temperature_column")
        or temperature_column
    )
    latitude = handle_deprecated_params(kwargs, "lat", "latitude") or latitude
    return_as_dataframe = (
        handle_deprecated_params(kwargs, "as_df", "return_as_dataframe")
        or return_as_dataframe
    )
    report_type = (
        handle_deprecated_params(kwargs, "report", "report_type") or report_type
    )

    # sub_df
    data = dataframe.loc[:, [temperature_column]]
    data_array = data.values

    # info_df
    nrows = data.shape[0]

    # initialization
    (P, ETo_x, C, ETo) = (np.zeros(nrows) for _ in range(4))

    # calculation
    temp = data_array[:, 0]
    month = data.index.month.values

    for i in range(nrows):
        P[i] = _BC_find_P(latitude, month[i])
        ETo_x[i] = _BC_ETo_x(P[i], temp[i])
        C[i] = _BC_find_C(month[i])
        ETo[i] = _BC_ETo(C[i], ETo_x[i])

    if report_type.lower() == "full":
        results = np.stack((month, temp, P, ETo_x, C, ETo), axis=1)
        columns_name = ["Month", "Temp", "P", "ETo_x", "C", "ETo"]
    elif report_type.lower() == "eto":
        results = ETo
        columns_name = ["ETo"]

    if return_as_dataframe:
        return pd.DataFrame(data=results, index=data.index, columns=columns_name)

    return results


@deprecated("eto_blaney_criddle")
def ETo_BlaneyCriddle(*args, **kwargs):
    """Calculate evapotranspiration (ETo) using the Blaney-Criddle method."""
    return eto_blaney_criddle(*args, **kwargs)


# Radiation


def _RAD_ETo(C, ETo_x):
    return C * ETo_x


def _RAD_ETo_x(w, Rs):
    return w * Rs


def _RAD_find_W(temp, table=t_rel_T_W):
    t = table["suhu"].values
    w = table["W"].values
    return np.interp(temp, t, w)


def _RAD_find_Rg(latitude, month, table=t_val_Rg):
    m = table.loc[month].values
    x = [-5, -4, -2, 0, 2, 4, 6, 8, 10]
    return np.interp(__lat_to_num(latitude), x, m)


def _RAD_Rs(sun_duration, Rg):
    return (0.25 + 0.54 * sun_duration / 100) * Rg


def _RAD_find_C(month, table=t_cor_C_RAD, col="C"):
    return table.loc[month, col]


def eto_radiation(
    dataframe,
    temperature_column,
    sunlight_column,
    latitude,
    return_as_dataframe=True,
    report_type="ETo",
    **kwargs
):
    """
    Calculate evapotranspiration (ETo) using radiation-based method.

    Parameters:
    - dataframe (pd.DataFrame): The input dataframe containing weather data.
    - temperature_column (str): The name of the column in the dataframe that represents temperature.
    - sunlight_column (str): The name of the column in the dataframe that represents sunlight.
    - latitude (str): The latitude of the location.
    - return_as_dataframe (bool, optional): Whether to return the result as a dataframe.
        Defaults to True.
    - report_type (str, optional): The type of report to generate.
        Options are "ETo" (default), "full", or "eto".
    - **kwargs: Additional keyword arguments for backward compatibility.

    Returns:
    - If return_as_dataframe is True, returns a pandas DataFrame with the calculated ETo values.
    - If return_as_dataframe is False, returns a numpy array or a single value
        (depending on the report_type).

    Note:
    - The input dataframe should contain columns for temperature and sunlight.
    - The temperature should be in degrees Celsius.
    - The sunlight should be in hours per day.
    - The latitude should be in decimal degrees.

    Deprecated Parameters:
    - df (pd.DataFrame): Deprecated, use dataframe instead.
    - temp_col (str): Deprecated, use temperature_column instead.
    - sun_col (str): Deprecated, use sunlight_column instead.
    - lat (str): Deprecated, use latitude instead.
    - as_df (bool): Deprecated, use return_as_dataframe instead.
    - report (str): Deprecated, use report_type instead.
    """
    # backward compatibility
    dataframe = handle_deprecated_params(kwargs, "df", "dataframe") or dataframe
    temperature_column = (
        handle_deprecated_params(kwargs, "temp_col", "temperature_column")
        or temperature_column
    )
    sunlight_column = (
        handle_deprecated_params(kwargs, "sun_col", "sunlight_column")
        or sunlight_column
    )
    latitude = handle_deprecated_params(kwargs, "lat", "latitude") or latitude
    return_as_dataframe = (
        handle_deprecated_params(kwargs, "as_df", "return_as_dataframe")
        or return_as_dataframe
    )
    report_type = (
        handle_deprecated_params(kwargs, "report", "report_type") or report_type
    )

    # sub_df
    weather_data = dataframe.loc[:, [temperature_column, sunlight_column]]
    weather_data_array = weather_data.values

    # info_df
    num_rows = weather_data.shape[0]

    # initialization
    (w, Rg, Rs, ETo_x, C, ETo) = (np.zeros(num_rows) for _ in range(6))

    # calculation
    temp = weather_data_array[:, 0]
    sun = weather_data_array[:, 1]
    month = weather_data.index.month.values

    for i in range(num_rows):
        w[i] = _RAD_find_W(temp[i])
        Rg[i] = _RAD_find_Rg(latitude, month[i])
        Rs[i] = _RAD_Rs(sun[i], Rg[i])
        ETo_x[i] = _RAD_ETo_x(w[i], Rs[i])
        C[i] = _RAD_find_C(month[i])
        ETo[i] = _RAD_ETo(C[i], ETo_x[i])

    if report_type.lower() == "full":
        results = np.stack((month, temp, sun, w, Rg, Rs, ETo_x, C, ETo), axis=1)
        columns_name = ["Month", "Temp", "Sun", "W", "R_G", "R_s", "ETo_x", "C", "ETo"]
    elif report_type.lower() == "eto":
        results = ETo
        columns_name = ["ETo"]

    if return_as_dataframe:
        return pd.DataFrame(
            data=results, index=weather_data.index, columns=columns_name
        )

    return results


@deprecated("eto_radiation")
def ETo_Radiation(*args, **kwargs):
    """Calculate evapotranspiration (ETo) using the Radiation method."""
    return eto_radiation(*args, **kwargs)


# PENMAN


def _PEN_ETo(C, ETo_x):
    return C * ETo_x


def _PEN_ETo_x(w, Rs, Rn1, fU, e_g, e_d):
    return w * (0.75 * Rs - Rn1) + (1 - w) * fU * (e_g - e_d)


def _PEN_Rs(sun_duration, RG):
    return (0.25 + 0.54 * sun_duration / 100) * RG


def _PEN_Rn1(ft, fe_d, fsun):
    return ft * fe_d * fsun


def _PEN_fe_d(e_d):
    return 0.34 - 0.044 * np.sqrt(e_d)


def _PEN_e_d(e_d, RH):
    return e_d * RH / 100


def _PEN_fsun(sun_duration):
    return 0.1 + (0.9 * sun_duration / 100)


def _PEN_fU(U):
    return 0.27 * (1 + 0.864 * U)


def _PEN_find_from_T(temp, table=t_rel_T_PEN):
    t = table["suhu"].values
    e = table["e_mbar"].values
    w = table["w"].values
    ft = table["f_t"].values

    return (np.interp(temp, t, e), np.interp(temp, t, w), np.interp(temp, t, ft))


def _PEN_find_Rg(latitude, month, table=t_val_Rg):
    m = table.loc[month].values
    x = [-5, -4, -2, 0, 2, 4, 6, 8, 10]
    return np.interp(__lat_to_num(latitude), x, m)


def _PEN_find_C(month, table=t_cor_C_PEN, col="C"):
    return table.loc[month, col]


def eto_penman(
    dataframe,
    temperature_column,
    humidity_column,
    wind_speed_column,
    sunlight_column,
    latitude,
    return_as_dataframe=True,
    report_type="ETo",
    **kwargs
):
    """
    Calculate evapotranspiration (ETo) using the Penman method.

    Parameters:
        dataframe (pd.DataFrame): The input dataframe containing weather data.
        temperature_column (str): The column name for temperature data in the dataframe.
        humidity_column (str): The column name for humidity data in the dataframe.
        wind_speed_column (str): The column name for wind speed data in the dataframe.
        sunlight_column (str): The column name for sunlight data in the dataframe.
        latitude (str): The latitude of the location.
        return_as_dataframe (bool, optional): Whether to return the results as a dataframe. 
            Defaults to True.
        report_type (str, optional): The type of report to generate. Can be "ETo" or "full". 
            Defaults to "ETo".
        **kwargs: Additional keyword arguments for deprecated parameters.

    Returns:
        pd.DataFrame or np.ndarray: The calculated reference evapotranspiration (ETo) values.

    Deprecated Parameters:
        df (pd.DataFrame): Deprecated parameter for the input dataframe.
        temp_col (str): Deprecated parameter for the temperature column name.
        humid_col (str): Deprecated parameter for the humidity column name.
        wind_col (str): Deprecated parameter for the wind speed column name.
        sun_col (str): Deprecated parameter for the sunlight column name.
        lat (str): Deprecated parameter for the latitude.
        as_df (bool): Deprecated parameter for return_as_dataframe.
        report (str): Deprecated parameter for report_type.
    """

    # handle deprecated parameters
    dataframe = handle_deprecated_params(kwargs, "df", "dataframe") or dataframe
    temperature_column = (
        handle_deprecated_params(kwargs, "temp_col", "temperature_column")
        or temperature_column
    )
    humidity_column = (
        handle_deprecated_params(kwargs, "humid_col", "humidity_column")
        or humidity_column
    )
    wind_speed_column = (
        handle_deprecated_params(kwargs, "wind_col", "wind_speed_column")
        or wind_speed_column
    )
    sunlight_column = (
        handle_deprecated_params(kwargs, "sun_col", "sunlight_column")
        or sunlight_column
    )
    latitude = handle_deprecated_params(kwargs, "lat", "latitude") or latitude
    return_as_dataframe = (
        handle_deprecated_params(kwargs, "as_df", "return_as_dataframe")
        or return_as_dataframe
    )
    report_type = (
        handle_deprecated_params(kwargs, "report", "report_type") or report_type
    )

    # sub_df
    weather_data = dataframe.loc[
        :, [temperature_column, humidity_column, wind_speed_column, sunlight_column]
    ]
    weather_data_array = weather_data.values

    # info_df
    num_rows = weather_data.shape[0]

    # initialization
    (e_g, w, ft, fed, e_d, Rg, Rs, fsun, fU, Rn1, C, ETo_x, ETo) = (
        np.zeros(num_rows) for _ in range(13)
    )

    # calculation
    temp = weather_data_array[:, 0]
    RH = weather_data_array[:, 1]
    wind = weather_data_array[:, 2]
    sun = weather_data_array[:, 3]
    month = weather_data.index.month.values

    for i in range(num_rows):
        e_g[i], w[i], ft[i] = _PEN_find_from_T(temp[i])
        e_d[i] = _PEN_e_d(e_g[i], RH[i])
        fed[i] = _PEN_fe_d(e_d[i])
        Rg[i] = _PEN_find_Rg(latitude, month[i])
        Rs[i] = _PEN_Rs(sun[i], Rg[i])
        fsun[i] = _PEN_fsun(sun[i])
        fU[i] = _PEN_fU(wind[i])
        Rn1[i] = _PEN_Rn1(ft[i], fed[i], fsun[i])
        C[i] = _PEN_find_C(month[i])
        ETo_x[i] = _PEN_ETo_x(w[i], Rs[i], Rn1[i], fU[i], e_g[i], e_d[i])
        ETo[i] = _PEN_ETo(C[i], ETo_x[i])

    if report_type.lower() == "full":
        results = np.stack(
            (
                month,
                temp,
                RH,
                wind,
                sun,
                e_g,
                w,
                ft,
                e_d,
                fed,
                Rg,
                Rs,
                fsun,
                fU,
                Rn1,
                C,
                ETo_x,
                ETo,
            ),
            axis=1,
        )
        column_names = [
            "Month",
            "Temp",
            "Humidity",
            "Wind",
            "Sun",
            "e_g",
            "w",
            "f_t",
            "e_d",
            "f_e_d",
            "R_g",
            "R_s",
            "f_sun",
            "f_U",
            "R_n1",
            "C",
            "ETo_x",
            "ETo",
        ]
    elif report_type.lower() == "eto":
        results = ETo
        column_names = ["ETo"]

    if return_as_dataframe:
        return pd.DataFrame(data=results, index=weather_data.index, columns=column_names)

    return results


@deprecated('eto_penman')
def ETo_Penman(*args, **kwargs):
    """Calculate evapotranspiration (ETo) using the Penman method."""
    return eto_penman(*args, **kwargs)
