"""Module for data preparation.

Use this module for preparation data in modeling of deep learning.
"""
# New format 20181007

import pandas as pd
import pathlib
from calendar import monthrange

# CHECK AND WARNING


# STAGE SCANNING
def _file_year(file, template='phderi'):
    file = pathlib.Path(file)
    if template == 'phderi':
        return int(file.stem.split()[0])
    return None


def _file_name(file, template='phderi', ixn=-2):
    file = pathlib.Path(file)
    if template == 'phderi':
        return ''.join(file.stem.split()[ixn:])
    return None

# STAGE GET


def _table_index(dataframe_raw, template='phderi'):
    template_check = {'phderi': ['Jan', 'Feb'],
                      'pdderi': ['JAN', 'FEB']}
    target, check = template_check[template]
    index = []
    for column in dataframe_raw:
        target_status = dataframe_raw[column].astype(str).str.contains(
            '^' + target + '$'
        ).sum()
        if target_status:
            index.append(column)
            break
    column = index[0]
    row_target = dataframe_raw[column] == target

    index.append(dataframe_raw[column][row_target].index.values.astype(int)[0])
    kolom, baris = index[0], index[1]
    if dataframe_raw.iloc[baris, kolom + 1] == check:
        dataframe_raw.iloc[baris + 1:baris + 32, kolom:kolom + 12]
    else:
        raise Exception(f'Format tidak sesuai dengan {format}')

    return index


def get_rawdf(singlefile, template='phderi'):
    singlefile = pathlib.Path(singlefile)
    if template == 'phderi' or template == 'pdderi':
        xl = pd.read_excel(singlefile, sheet_name=0, header=None)
        table_index = _table_index(xl, template)
        kolom, baris = table_index[0], table_index[1]
        rawdf = xl.iloc[baris + 1:baris + 32, kolom:kolom + 12]
        return rawdf


# STAGE TRANSFORM
def tf_emptydf(year):
    """ Creating emptydf with index of date in single year """
    start, end = map(pd.Timestamp, f'{year}0101 {year}1231'.split())

    df = pd.DataFrame()
    df['date'] = pd.date_range(start, end)
    df.set_index('date', inplace=True)
    return df


def tf_column(tabledf, year):
    """ Return in single column """
    month = 1
    data_column = []

    for column in tabledf:
        days = monthrange(year, month)[1]
        end = 31 if (days == 31) else (days - 31)
        data_column += tabledf[column][:end].tolist()
        month += 1

    return data_column


def tf_rawdf(rawdf, year, name='ch'):
    """ Transform rawdf to single column dataframe"""
    maindf = tf_emptydf(year)
    data = tf_column(rawdf, year)
    maindf[name] = data
    return maindf


# STAGE JOIN
