"""manual:
https://gist.github.com/taruma/a9dd4ea61db2526853b99600909e9c50"""

from calendar import isleap
from collections import defaultdict
from pathlib import Path
import pandas as pd
import numpy as np


def _get_years(io):
    excel = pd.ExcelFile(io)
    years = []
    for sheet in excel.sheet_names:
        if sheet.isdigit():
            years.append(int(sheet))
    return sorted(years)


def _get_pivot(io, year, fmt):

    if fmt == 'uma.debit':
        return pd.read_excel(
            io, sheet_name=str(year),
            header=None, usecols='AN:AY'
        ).iloc[16:47, :]

    if fmt == 'uma.hujan':
        return pd.read_excel(
            io, sheet_name=str(year),
            header=None, usecols='B:M'
        ).iloc[19:50, :]


def _get_data_oneyear(io, year, fmt):
    _drop = [59, 60, 61, 123, 185, 278, 340]
    _drop_leap = [60, 61, 123, 185, 278, 340]

    pivot_table = _get_pivot(io, str(year), fmt=fmt)
    data = pivot_table.melt().drop('variable', axis=1)
    if isleap(year):
        return data['value'].drop(_drop_leap).values
    return data['value'].drop(_drop).values


def _get_data_allyear(io, fmt, aslist=False):
    list_years = _get_years(io)

    data_each_year = []

    for year in list_years:
        data = _get_data_oneyear(io, year=year, fmt=fmt)
        data_each_year.append(data)

    if aslist:
        return data_each_year

    return np.hstack(data_each_year)


def _get_invalid(array, check):
    dict_invalid = defaultdict(list)
    for index, element in enumerate(array):
        try:
            check(element)
            if np.isnan(check(element)):
                dict_invalid['NaN'] += [index]
        except ValueError:
            dict_invalid[element] += [index]

    return dict(dict_invalid)


def _have_invalid(array, check):
    return bool(_get_invalid(array, check=check))


def _check_invalid(array, check=np.float):
    if _have_invalid(array, check=check):
        return _get_invalid(array, check=check)
    return None


def read_folder(dataset_path, pattern, fmt, prefix='', invalid=False):
    dataset_path = Path(dataset_path)
    total_files = len(list(dataset_path.glob(pattern)))
    print(f'Found {total_files} file(s)')

    data_allstation = {}
    data_invalid = {}

    for counter, file in enumerate(dataset_path.glob(pattern)):
        print(f':: {counter + 1:^4}:\t{file.name:s}')
        station_name = prefix + '_'.join(file.stem.split('_')[1:-2])
        data_each_station = _get_data_allyear(file, fmt=fmt)
        data_allstation[station_name] = data_each_station
        if invalid:
            data_invalid[station_name] = _check_invalid(data_each_station)

    if invalid:
        return data_allstation, data_invalid
    return data_allstation
