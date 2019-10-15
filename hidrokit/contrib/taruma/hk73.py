"""manual:
https://gist.github.com/taruma/b00880905f297013f046dad95dc2e284"""

import pandas as pd
import numpy as np
from operator import itemgetter
from itertools import groupby


def _read_bmkg(io):
    return pd.read_excel(
        io, skiprows=8, skipfooter=16, header=0, index_col=0, parse_dates=True,
        date_parser=lambda x: pd.to_datetime(x, format='%d-%m-%Y')
    )


def _have_nan(dataset):
    if dataset.isna().any().any():
        return True
    else:
        return False


def _get_index1D(array1D_bool):
    return np.argwhere(array1D_bool).reshape(-1,)


def _get_nan(dataset):
    nan = {}

    for col in dataset.columns:
        nan[col] = _get_index1D(dataset[col].isna().values).tolist()

    return nan


def _get_missing(dataset):
    missing = {}

    for col in dataset.columns:
        masking = (dataset[col] == 8888) | (dataset[col] == 9999)
        missing[col] = _get_index1D(masking.values)

    return missing


def _check_nan(dataset):
    if _have_nan(dataset):
        return _get_nan(dataset)
    else:
        return None


def _get_nan_columns(dataset):
    return dataset.columns[dataset.isna().any()].tolist()


def _group_as_list(array):

    # based on https://stackoverflow.com/a/15276206
    group_list = []
    for _, g in groupby(enumerate(array), lambda x: x[0] - x[1]):
        single_list = sorted(list(map(itemgetter(1), g)))
        group_list.append(single_list)

    return group_list


def _group_as_index(
    group_list, index=None, date_format='%Y%m%d',
    format_date='{}-{}'
):
    group_index = []
    date_index = isinstance(index, pd.DatetimeIndex)

    for item in group_list:
        if len(item) == 1:
            if date_index:
                group_index.append(index[item[0]].strftime(date_format))
            else:
                group_index.append(index[item[0]])
        else:
            if date_index:
                group_index.append(
                    format_date.format(
                        index[item[0]].strftime(date_format),
                        index[item[-1]].strftime(date_format)
                    )
                )
            else:
                group_index.append(
                    format_date.format(
                        index[item[0]], index[item[-1]]
                    )
                )

    return group_index
