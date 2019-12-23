"""manual:
https://gist.github.com/taruma/7f81cf0fea5250cfe47942b4e16a8a65"""

import numpy as np
import pandas as pd

t_rel_P_LL = pd.DataFrame({
    '5 U': [0.27] * 3 + [0.28] * 6 + [0.27] * 3,
    '2.5 U': [0.27] * 3 + [0.28] * 6 + [0.27] * 3,
    '0': [.27] * 12,
    '2.5 S': [.28] * 12,
    '5 S': [.28] * 12,
    '7.5 S': [.28] * 4 + [.27] * 4 + [.28] * 3 + [.29] * 1,
    '10 S': [.29] + [.28] * 2 + [.27] + [.26] * 4 + [.27] + [.28] * 2 + [.29]
}, index=range(1, 13))

t_cor_C_BC = pd.DataFrame({
    'C': [.8, .8, .75, .7, .7, .7, .7, .75, .8, .8, .8, .8]
}, index=range(1, 13))

t_rel_T_W = pd.DataFrame({
    'suhu': np.arange(24.0, 30, 0.2),
    'W': np.arange(0.735, 0.794, .002)
})

t_cor_C_RAD = pd.DataFrame(
    {'C': [.8] * 2 + [.75] * 5 + [.8] * 5},
    index=range(1, 13))

_data = [13.0, 14.3, 14.7, 15.0, 15.3, 15.5, 15.8, 16.1, 16.1,
         14.0, 15.0, 15.3, 15.5, 15.7, 15.8, 16.0, 16.1, 16.0,
         15.0, 15.5, 15.6, 15.7, 15.7, 15.6, 15.6, 15.1, 15.3,
         15.1, 15.5, 15.3, 15.3, 15.1, 14.9, 14.7, 14.1, 14.0,
         15.3, 14.9, 14.6, 14.4, 14.1, 13.8, 13.4, 13.1, 12.6,
         15.0, 14.4, 14.2, 13.9, 13.9, 13.2, 12.8, 12.4, 12.6,
         15.1, 14.6, 14.3, 14.1, 14.1, 13.4, 13.1, 12.7, 11.8,
         15.3, 15.1, 14.9, 14.8, 14.8, 14.3, 14.0, 13.7, 12.2,
         15.1, 15.3, 15.3, 15.3, 15.3, 15.1, 15.0, 14.9, 13.1,
         15.7, 15.1, 15.3, 15.4, 15.4, 15.6, 15.7, 15.8, 14.6,
         14.8, 14.5, 14.8, 15.1, 15.1, 15.5, 15.8, 16.0, 15.6,
         14.6, 14.1, 14.4, 14.8, 14.8, 15.4, 15.7, 16.0, 16.0]
_data = np.array(_data).reshape((12, 9)).T
t_val_Rg = pd.DataFrame(_data,
                        columns=range(1, 13),
                        index=['5 LU', '4 LU', '2 LU', '0',
                               '2 LS', '4 LS', '6 LS', '8 LS',
                               '10 LS']).T

t_cor_C_PEN = pd.DataFrame({
    'C': [1.1] * 3 + [.9] * 4 + [1.1] * 5,
}, index=range(1, 13))

t_rel_T_PEN = pd.DataFrame({
    'suhu': np.arange(24., 29.1, .2),
    'e_mbar': [29.85, 30.21, 30.57, 30.94, 31.31, 31.69, 32.06, 32.45, 32.83,
               32.22, 33.62, 34.02, 34.42, 34.83, 35.25, 35.66, 36.09, 36.50,
               36.94, 37.37, 37.81, 38.25, 38.70, 39.14, 39.61, 40.06],
    'w': np.arange(0.735, 0.786, .002),
    'f_t': [15.40, 15.45, 15.50, 15.55, 15.60, 15.65, 15.70, 15.75, 15.80,
            15.85, 15.90, 15.94, 15.98, 16.02, 16.06, 16.10, 16.14, 16.18,
            16.22, 16.26, 16.30, 16.34, 16.38, 16.42, 16.46, 16.5]
})


def __lat_to_num(lat):
    num, lat = lat.split(' ')
    num = float(num)
    num = -num if lat.lower() == 'lu' else num
    return num

# Blaney Criddle


def BC_ETo(c, ETo_x):
    return c * ETo_x


def BC_ETo_x(P, temp):
    return P * (.457 * temp + 8.13)


def BC_find_P(latitude, month, table=t_rel_P_LL):
    m = table.loc[month].values
    x = [-5, -2.5, 0, 2.5, 5, 7.5, 10]
    return np.interp(__lat_to_num(latitude), x, m)


def BC_find_C(month, table=t_cor_C_BC, col='C'):
    return table.loc[month, col]


def ETo_BlaneyCriddle(df, temp_col, lat,
                      as_df=True, report='ETo'):

    # sub_df
    data = df.loc[:, [temp_col]]
    data_array = data.values

    # info_df
    nrows = data.shape[0]

    # initialization
    (P, ETo_x, C, ETo) = (np.zeros(nrows) for _ in range(4))

    # calculation
    temp = data_array[:, 0]
    month = data.index.month.values

    for i in range(nrows):
        P[i] = BC_find_P(lat, month[i])
        ETo_x[i] = BC_ETo_x(P[i], temp[i])
        C[i] = BC_find_C(month[i])
        ETo[i] = BC_ETo(C[i], ETo_x[i])

    if report.lower() == 'full':
        results = np.stack((
            month, temp, P, ETo_x, C, ETo
        ), axis=1)
        columns_name = [
            'Month', 'Temp', 'P', 'ETo_x', 'C', 'ETo'
        ]
    elif report.lower() == 'eto':
        results = ETo
        columns_name = ['ETo']

    if as_df:
        return pd.DataFrame(
            data=results, index=data.index, columns=columns_name
        )
    else:
        return results


# Radiation

def RAD_ETo(C, ETo_x):
    return C * ETo_x


def RAD_ETo_x(w, Rs):
    return w * Rs


def RAD_find_W(temp, table=t_rel_T_W):
    t = table['suhu'].values
    w = table['W'].values
    return np.interp(temp, t, w)


def RAD_find_Rg(latitude, month, table=t_val_Rg):
    m = table.loc[month].values
    x = [-5, -4, -2, 0, 2, 4, 6, 8, 10]
    return np.interp(__lat_to_num(latitude), x, m)


def RAD_Rs(sun_duration, Rg):
    return (0.25 + 0.54 * sun_duration / 100) * Rg


def RAD_find_C(month, table=t_cor_C_RAD, col='C'):
    return table.loc[month, col]


def ETo_Radiation(df, temp_col, sun_col, lat,
                  as_df=True, report='ETo'):

    # sub_df
    data = df.loc[:, [temp_col, sun_col]]
    data_array = data.values

    # info_df
    nrows = data.shape[0]

    # initialization
    (w, Rg, Rs, ETo_x, C, ETo) = (np.zeros(nrows) for _ in range(6))

    # calculation
    temp = data_array[:, 0]
    sun = data_array[:, 1]
    month = data.index.month.values

    for i in range(nrows):
        w[i] = RAD_find_W(temp[i])
        Rg[i] = RAD_find_Rg(lat, month[i])
        Rs[i] = RAD_Rs(sun[i], Rg[i])
        ETo_x[i] = RAD_ETo_x(w[i], Rs[i])
        C[i] = RAD_find_C(month[i])
        ETo[i] = RAD_ETo(C[i], ETo_x[i])

    if report.lower() == 'full':
        results = np.stack((
            month, temp, sun, w, Rg, Rs, ETo_x, C, ETo
        ), axis=1)
        columns_name = [
            'Month', 'Temp', 'Sun', 'W', 'R_G', 'R_s', 'ETo_x', 'C', 'ETo'
        ]
    elif report.lower() == 'eto':
        results = ETo
        columns_name = ['ETo']

    if as_df:
        return pd.DataFrame(
            data=results, index=data.index, columns=columns_name
        )
    else:
        return results


# PENMAN

def PEN_ETo(C, ETo_x):
    return C * ETo_x


def PEN_ETo_x(w, Rs, Rn1, fU, e_g, e_d):
    return w * (0.75 * Rs - Rn1) + (1 - w) * fU * (e_g - e_d)


def PEN_Rs(sun_duration, RG):
    return (0.25 + 0.54 * sun_duration / 100) * RG


def PEN_Rn1(ft, fe_d, fsun):
    return ft * fe_d * fsun


def PEN_fe_d(e_d):
    return 0.34 - 0.044 * np.sqrt(e_d)


def PEN_e_d(e_d, RH):
    return e_d * RH / 100


def PEN_fsun(sun_duration):
    return 0.1 + (0.9 * sun_duration / 100)


def PEN_fU(U):
    return 0.27 * (1 + 0.864 * U)


def PEN_find_from_T(temp, table=t_rel_T_PEN):
    t = table['suhu'].values
    e = table['e_mbar'].values
    w = table['w'].values
    ft = table['f_t'].values

    return (
        np.interp(temp, t, e),
        np.interp(temp, t, w),
        np.interp(temp, t, ft)
    )


def PEN_find_Rg(latitude, month, table=t_val_Rg):
    m = table.loc[month].values
    x = [-5, -4, -2, 0, 2, 4, 6, 8, 10]
    return np.interp(__lat_to_num(latitude), x, m)


def PEN_find_C(month, table=t_cor_C_PEN, col='C'):
    return table.loc[month, col]


def ETo_Penman(df, temp_col, humid_col, wind_col, sun_col, lat,
               as_df=True, report='ETo'):

    # sub_df
    data = df.loc[:, [temp_col, humid_col, wind_col, sun_col]]
    data_array = data.values

    # info_df
    nrows = data.shape[0]

    # initialization
    (e_g, w, ft, fed, e_d, Rg, Rs, fsun,
     fU, Rn1, C, ETo_x, ETo) = (np.zeros(nrows) for _ in range(13))

    # calculation
    temp = data_array[:, 0]
    RH = data_array[:, 1]
    wind = data_array[:, 2]
    sun = data_array[:, 3]
    month = data.index.month.values

    for i in range(nrows):
        e_g[i], w[i], ft[i] = PEN_find_from_T(temp[i])
        e_d[i] = PEN_e_d(e_g[i], RH[i])
        fed[i] = PEN_fe_d(e_d[i])
        Rg[i] = PEN_find_Rg(lat, month[i])
        Rs[i] = PEN_Rs(sun[i], Rg[i])
        fsun[i] = PEN_fsun(sun[i])
        fU[i] = PEN_fU(wind[i])
        Rn1[i] = PEN_Rn1(ft[i], fed[i], fsun[i])
        C[i] = PEN_find_C(month[i])
        ETo_x[i] = PEN_ETo_x(w[i], Rs[i], Rn1[i], fU[i], e_g[i], e_d[i])
        ETo[i] = PEN_ETo(C[i], ETo_x[i])

    if report.lower() == 'full':
        results = np.stack((
            month, temp, RH, wind, sun, e_g, w, ft, e_d, fed, Rg, Rs,
            fsun, fU, Rn1, C, ETo_x, ETo
        ), axis=1)
        columns_name = [
            'Month', 'Temp', 'Humidity', 'Wind', 'Sun', 'e_g', 'w', 'f_t',
            'e_d', 'f_e_d', 'R_g', 'R_s', 'f_sun', 'f_U', 'R_n1', 'C', 'ETo_x',
            'ETo'
        ]
    elif report.lower() == 'eto':
        results = ETo
        columns_name = ['ETo']

    if as_df:
        return pd.DataFrame(
            data=results, index=data.index, columns=columns_name
        )
    else:
        return results
