"""Module for data preparation.

Use this module for preparation data in modeling of deep learning.
"""
# New format 20181007

import pandas as pd
import pathlib
from calendar import monthrange

# STAGE SCANNING


def _file_year(file, template='phderi'):
    file = pathlib.Path(file)
    if template == 'phderi':
        return int(file.stem.split()[0])


# def _file_name(file, template='phderi', ixn=-2):
#     file = pathlib.Path(file)
#     if template == 'phderi':
#         return ''.join(file.stem.split()[ixn:])


def _cell_index(dataframe, template='phderi'):
    """Return cell index (column, row) of first value on pivot.

    Parameters
    ----------
    dataframe : DataFrame
        Raw dataframe imported from excel
    template : str, optional
        Template, by default 'phderi'

    Returns
    -------
    list
        Return [column index, row index]

    Raises
    ------
    Exception
        Not match with template.
    """
    template_check = {'phderi': ['Jan', 'Feb'],
                      'pdderi': ['JAN', 'FEB']}
    target, check = template_check[template]
    cell_index = []
    for column in dataframe:
        target_status = dataframe[column].astype(str).str.contains(
            '^' + target + '$'
        ).sum()
        if target_status:
            cell_index.append(column)
            break
    column = cell_index[0]
    row_target = dataframe[column] == target

    cell_index.append(dataframe[column]
                      [row_target].index.values.astype(int)[0])
    column, row = cell_index[0], cell_index[1]
    if dataframe.iloc[row, column + 1] == check:
        return cell_index
    else:
        raise Exception(f'Format tidak sesuai dengan {format}')


def _file_single_pivot(file, template='phderi'):
    """Return pivot table inside file

    Parameters
    ----------
    file : str
        File path
    template : str, optional
        Template, by default 'phderi'

    Returns
    -------
    Dataframe
        Pivot table
    """
    file = pathlib.Path(file)
    if template == 'phderi' or template == 'pdderi':
        dataframe = pd.read_excel(file, sheet_name=0, header=None)
        cell_index = _cell_index(dataframe, template)
        column, row = cell_index[0], cell_index[1]
        pivot = dataframe.iloc[row + 1:row + 32, column:column + 12]
        return pivot


def _dataframe_year(year):
    """Return empty dataframe with date index

    Parameters
    ----------
    year : int
        Year

    Returns
    -------
    Dataframe
        Empty dataframe with date index
    """

    start, end = map(pd.Timestamp, f'{year}0101 {year}1231'.split())

    return pd.DataFrame(index=pd.date_range(start, end))


def _dataframe_data(pivot, year):
    """Transform pivot table to list

    Parameters
    ----------
    pivot : DataFrame
        Pivot table
    year : int
        Year

    Returns
    -------
    list
        Return list of data
    """
    month = 1
    data = []

    for column in pivot:
        days = monthrange(year, month)[1]
        end = 31 if (days == 31) else (days - 31)
        data += pivot[column][:end].tolist()
        month += 1
    return data


def _dataframe_table(pivot, year, name='ch'):
    """Transform pivot table to single column dataframe.

    Parameters
    ----------
    pivot : DataFrame
        Pivot table
    year : int
        Year
    name : str, optional
        Column name, by default 'ch'

    Returns
    -------
    DataFrame
        Dataframe
    """
    table = _dataframe_year(year)
    data = _dataframe_data(pivot, year)
    table[name] = data
    return table

# @todo reshape pivot table
# @body cari tahu fungsi untuk mengubah pivot table, jadi fungsi diatas tidak
# @body diperlukan.
