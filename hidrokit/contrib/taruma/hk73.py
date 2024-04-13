"""manual:
https://gist.github.com/taruma/b00880905f297013f046dad95dc2e284"""

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


def _has_nan_values(dataframe):
    """
    Check if the given dataset contains any NaN values.

    Parameters:
        dataframe (pandas.DataFrame): The dataset to check for NaN values.

    Returns:
        bool: True if the dataset contains NaN values, False otherwise.
    """
    return bool(dataframe.isna().any().any())


def _get_missing_data_indices(nan_indicator_vector):
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


def _get_nan_indices_by_column(dataframe):
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
        nan[col] = _get_missing_data_indices(dataframe[col].isna().values).tolist()
    return nan


def _get_unrecorded_indices(dataframe):
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
        unrecorded_indices[col] = _get_missing_data_indices(masking.values)

    return unrecorded_indices


def _get_nan_indices_if_exists(dataframe):
    """
    Returns the indices of NaN values in the given dataframe if NaN values exist.

    Parameters:
        dataframe (pandas.DataFrame): The input dataframe.

    Returns:
        dict or None: A dictionary with keys as column names and values as lists of
            indices where missing values occur, or None if no NaN values exist.
    """
    if _has_nan_values(dataframe):
        return _get_nan_indices_by_column(dataframe)
    else:
        return None


def _get_columns_with_nan_values(dataframe):
    return dataframe.columns[dataframe.isna().any()].tolist()


def _group_consecutive_elements(input_list: List) -> List[List]:
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


def _format_group_indices(
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
    return _has_nan_values(*args, **kwargs)


@deprecated("_get_missing_data_indices")
def _get_index1D(*args, **kwargs):
    return _get_missing_data_indices(*args, **kwargs)


@deprecated("_get_nan_indices_by_column")
def _get_nan(*args, **kwargs):
    return _get_nan_indices_by_column(*args, **kwargs)


@deprecated("_get_unrecorded_indices")
def _get_missing(*args, **kwargs):
    return _get_unrecorded_indices(*args, **kwargs)


@deprecated("_get_nan_indices_if_exists")
def _check_nan(*args, **kwargs):
    return _get_nan_indices_if_exists(*args, **kwargs)


@deprecated("_get_columns_with_nan_values")
def _get_nan_columns(*args, **kwargs):
    return _get_columns_with_nan_values(*args, **kwargs)


@deprecated("_group_consecutive_elements")
def _group_as_list(*args, **kwargs):
    return _group_consecutive_elements(*args, **kwargs)


@deprecated("_format_group_indices")
def _group_as_index(*args, **kwargs):
    return _format_group_indices(*args, **kwargs)
