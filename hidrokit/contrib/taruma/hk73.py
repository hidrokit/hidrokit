"""
This module provides functions for reading and analyzing 
    BMKG (Meteorology, Climatology, and Geophysics Agency) data.

For more information, refer to the manual: 
    https://gist.github.com/taruma/b00880905f297013f046dad95dc2e284

Functions:
- read_bmkg_excel(io): Read BMKG data from an Excel file.
- has_nan_values(dataframe): Check if the given dataset contains any NaN values.
- get_missing_data_indices(nan_indicator_vector): Get the indices of missing data 
    in the given nan_indicator_vector.
- get_nan_indices_by_column(dataframe): Get the indices of missing values (NaN) 
    for each column in a DataFrame.
- get_unrecorded_indices(dataframe): Get the indices of unrecorded data in the given dataframe.
- get_nan_indices_if_exists(dataframe): Returns the indices of NaN values 
    in the given dataframe if NaN values exist.
- get_columns_with_nan_values(dataframe): Get the columns with NaN values in the given dataframe.
- group_consecutive_elements(input_list): Groups consecutive elements in the input list.
- format_group_indices(group_list, indices=None, format_date="%Y%m%d", date_range_format="{}-{}"): 
    Formats the group indices based on the given parameters.

Deprecated Functions:
- _read_bmkg(*args, **kwargs): Deprecated version of read_bmkg_excel.
- _have_nan(*args, **kwargs): Deprecated version of has_nan_values.
- _get_index1D(*args, **kwargs): Deprecated version of get_missing_data_indices.
- _get_nan(*args, **kwargs): Deprecated version of get_nan_indices_by_column.
- _get_missing(*args, **kwargs): Deprecated version of get_unrecorded_indices.
- _check_nan(*args, **kwargs): Deprecated version of get_nan_indices_if_exists.
- _get_nan_columns(*args, **kwargs): Deprecated version of get_columns_with_nan_values.
- _group_as_list(*args, **kwargs): Deprecated version of group_consecutive_elements.
- _group_as_index(group_list, index=None, date_format="%Y%m%d", format_date="{}-{}"): 
    Deprecated version of format_group_indices.
"""


from itertools import groupby
from operator import itemgetter
from typing import List
import pandas as pd
import numpy as np
from hidrokit.contrib.taruma.deprecated_func import deprecated


def read_bmkg_excel(io):
    """
    Read BMKG data from an Excel file.

    Parameters:
    - io: str or file-like object
        The file path or file-like object to read the Excel data from.

    Returns:
    - pandas.DataFrame
        The data read from the Excel file.

    """
    return pd.read_excel(
        io,
        skiprows=8,
        skipfooter=16,
        header=0,
        index_col=0,
        parse_dates=True,
        date_format="%d-%m-%Y",
    )


def has_nan_values(dataframe):
    """
    Check if the given dataset contains any NaN values.

    Parameters:
        dataframe (pandas.DataFrame): The dataset to check for NaN values.

    Returns:
        bool: True if the dataset contains NaN values, False otherwise.
    """
    return bool(dataframe.isna().any().any())


def get_missing_data_indices(nan_indicator_vector):
    """
    Get the indices of missing data in the given nan_indicator_vector.

    Parameters:
        nan_indicator_vector (numpy.ndarray): A boolean array indicating missing data.

    Returns:
        numpy.ndarray: An array of indices where missing data is present.
    """
    return np.argwhere(nan_indicator_vector).reshape(
        -1,
    )


def get_nan_indices_by_column(dataframe):
    """
    Get the indices of missing values (NaN) for each column in a DataFrame.

    Parameters:
        dataframe (pandas.DataFrame): The input DataFrame.

    Returns:
        dict: A dictionary where the keys are the column names and the values are lists of indices
            where missing values occur in each column.
    """
    nan = {}
    for col in dataframe.columns:
        nan[col] = get_missing_data_indices(dataframe[col].isna().values).tolist()
    return nan


def get_unrecorded_indices(dataframe):
    """
    Get the indices of unrecorded data in the given dataframe.

    Parameters:
        dataframe (pandas.DataFrame): The input dataframe.

    Returns:
        dict: A dictionary where the keys are the column names and the values are
            the indices of unrecorded data in each column.
    """
    unrecorded_indices = {}

    for col in dataframe.columns:
        masking = (dataframe[col] == 8888) | (dataframe[col] == 9999)
        unrecorded_indices[col] = get_missing_data_indices(masking.values)

    return unrecorded_indices


def get_nan_indices_if_exists(dataframe):
    """
    Returns the indices of NaN values in the given dataframe if NaN values exist.

    Parameters:
        dataframe (pandas.DataFrame): The input dataframe.

    Returns:
        dict or None: A dictionary with keys as column names and values as lists of
            indices where missing values occur, or None if no NaN values exist.
    """
    if has_nan_values(dataframe):
        return get_nan_indices_by_column(dataframe)
    else:
        return None


def get_columns_with_nan_values(dataframe):
    return dataframe.columns[dataframe.isna().any()].tolist()


def group_consecutive_elements(input_list: List) -> List[List]:
    """
    Groups consecutive elements in the input list.

    Args:
        input_list (List): The list of elements to be grouped.

    Returns:
        List[List]: A list of lists, where each inner list contains consecutive elements
            from the input list.

    Example:
        >>> input_list = [1, 2, 3, 5, 6, 8, 9]
        >>> _group_consecutive_elements(input_list)
        [[1, 2, 3], [5, 6], [8, 9]]
    """
    # based on https://stackoverflow.com/a/15276206
    group_list = []
    for _, g in groupby(enumerate(input_list), lambda x: x[0] - x[1]):
        single_list = sorted(list(map(itemgetter(1), g)))
        group_list.append(single_list)
    return group_list


def format_group_indices(
    group_list, indices=None, format_date="%Y%m%d", date_range_format="{}-{}"
):
    """
    Formats the group indices based on the given parameters.

    Args:
        group_list (list): The list of groups.
        indices (pd.Index or pd.DatetimeIndex, optional): The indices to format. Defaults to None.
        format_date (str, optional): The date format string. Defaults to "%Y%m%d".
        date_range_format (str, optional): The format string for date ranges. Defaults to "{}-{}".

    Returns:
        list: The formatted group indices.
    """
    formatted_indices = []
    is_date_index = isinstance(indices, pd.DatetimeIndex)

    for item in group_list:
        if len(item) == 1:
            if is_date_index:
                formatted_indices.append(indices[item[0]].strftime(format_date))
            else:
                formatted_indices.append(indices[item[0]])
        else:
            if is_date_index:
                formatted_indices.append(
                    date_range_format.format(
                        indices[item[0]].strftime(format_date),
                        indices[item[-1]].strftime(format_date),
                    )
                )
            else:
                formatted_indices.append(
                    date_range_format.format(indices[item[0]], indices[item[-1]])
                )

    return formatted_indices


# for backward compatibility
@deprecated("read_bmkg_excel")
def _read_bmkg(*args, **kwargs):
    return read_bmkg_excel(*args, **kwargs)


@deprecated("_has_nan_values")
def _have_nan(*args, **kwargs):
    return has_nan_values(*args, **kwargs)


@deprecated("_get_missing_data_indices")
def _get_index1D(*args, **kwargs):  # pylint: disable=invalid-name
    return get_missing_data_indices(*args, **kwargs)


@deprecated("_get_nan_indices_by_column")
def _get_nan(*args, **kwargs):
    return get_nan_indices_by_column(*args, **kwargs)


@deprecated("_get_unrecorded_indices")
def _get_missing(*args, **kwargs):
    return get_unrecorded_indices(*args, **kwargs)


@deprecated("_get_nan_indices_if_exists")
def _check_nan(*args, **kwargs):
    return get_nan_indices_if_exists(*args, **kwargs)


@deprecated("_get_columns_with_nan_values")
def _get_nan_columns(*args, **kwargs):
    return get_columns_with_nan_values(*args, **kwargs)


@deprecated("_group_consecutive_elements")
def _group_as_list(*args, **kwargs):
    return group_consecutive_elements(*args, **kwargs)


@deprecated("_format_group_indices")
def _group_as_index(
    group_list, index=None, date_format="%Y%m%d", format_date="{}-{}"
):
    return format_group_indices(
        group_list,
        indices=index,
        format_date=date_format,
        date_range_format=format_date,
    )
