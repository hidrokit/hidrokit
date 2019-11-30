"""manual:
https://gist.github.com/taruma/05dab67fac8313a94134ac02d0398897
"""

import pandas as pd
import numpy as np
from calendar import monthrange
from hidrokit.contrib.taruma import hk43


# ref: https://www.reddit.com/r/learnpython/comments/485h1p/
from collections.abc import Sequence


def _index_hourly(year, freq='60min'):
    """Create DatetimeIndex with specific year or [year_start, year_end]"""
    if isinstance(year, Sequence):
        year_start, year_end = year
    else:
        year_start, year_end = year, year

    period = '{}0101 00:00,{}1231 23:00'.format(
        year_start, year_end).split(',')
    return pd.date_range(*period, freq=freq)


def _melt_to_array(df):
    return df.melt().drop('variable', axis=1)['value'].values


def _get_array_in_month(df, year, month):
    n_days = monthrange(year, month)[1]
    mask_month = slice(None, n_days)
    df_month = df.iloc[mask_month, :].T
    return _melt_to_array(df_month)


def _get_year(df, loc=(0, 1)):
    return df.iloc[loc]


def _get_array_in_year(df, year):
    n_rows, _ = df.shape

    # configuration (view the excel)
    n_month = 1  # number of row to monthID
    n_gap = 2  # number of row between month pivot table
    n_lines = 31 + n_gap  # number of row each month

    data = []
    for row in range(1, n_rows, n_lines):
        mask_start = row + n_month
        mask_end = row + n_lines

        month = df.iloc[mask_start, 1]
        mask_row = slice(mask_start, mask_end)

        df_month = df.iloc[mask_row, 4:]
        array_month = _get_array_in_month(df_month, year, month)
        data.append(array_month)

    return np.hstack(data)


def _get_info(file, config_sheet=None):
    excel = pd.ExcelFile(file)
    first_sheet = excel.sheet_names[0]
    config_sheet = first_sheet if config_sheet is None else config_sheet

    df = pd.read_excel(
        excel, sheet_name=config_sheet, header=None, usecols='A:B'
    )
    info = {}

    for index, _ in df.iterrows():
        key = df.iloc[index, 0].lower()
        value = df.iloc[index, 1]
        info[str(key)] = value

    return info


def read_excel_hourly(file, station=None):
    excel = pd.ExcelFile(file)

    # CONFIG
    years = hk43._get_years(excel)
    station = 'NA' if station is None else station

    # READ DATA
    data = []
    for year in years:
        sheet = pd.read_excel(
            excel, sheet_name=str(year),
            header=None, nrows=396,
            usecols='A:AB'
        )
        array = _get_array_in_year(sheet, year)
        df_year = pd.DataFrame(
            data=array,
            columns=[station],
            index=_index_hourly(year)
        )
        data.append(df_year)

    return pd.concat(data, axis=0)
