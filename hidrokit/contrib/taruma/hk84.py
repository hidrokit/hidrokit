"""
hk84: summary_hourly
This module provides functions for generating a summary of hourly data from a DataFrame.

Functions:
- summary_hourly(
    dataframe, column, n_hours=24, 
    text_date=None, return_as_dataframe=True, 
    date_format="%Y-%m-%d", hour_format="%H:%M"): 
        Generate a summary of hourly data from a DataFrame.

    Args:
        dataframe (pandas.DataFrame): The input DataFrame.
        column (str): The name of the column containing the hourly data.
        n_hours (int, optional): The number of hours to group together. Defaults to 24.
        text_date (list, optional): The list of column names to include in the summary. 
            Defaults to ['date', 'hour'].
        return_as_dataframe (bool, optional): Whether to return the summary as a DataFrame. 
            Defaults to True.
        date_format (str, optional): The date format string. Defaults to '%Y-%m-%d'.
        hour_format (str, optional): The hour format string. Defaults to '%H:%M'.

    Returns:
        pandas.DataFrame or dict: The summary of hourly data. 
            If `return_as_dataframe` is True, a DataFrame is returned. 
            Otherwise, a dictionary is returned.

manual:
    https://gist.github.com/taruma/cad07f29ffc025ba9e7801e752be3444
"""

import pandas as pd
from hidrokit.contrib.taruma import hk73


def _time_grouped(df, index_grouped, col, date_fmt="%Y-%m-%d", hour_fmt="%H:%M"):
    """
    Return index_grouped as (list of date, list of hour)

    Parameters:
    - df: pandas DataFrame
        The DataFrame containing the data.
    - index_grouped: list of tuples
        The index groups to be processed.
    - col: int or str
        The column index or name to extract the date and hour values from.
    - date_fmt: str, optional
        The format string for the date values. Default is '%Y-%m-%d'.
    - hour_fmt: str, optional
        The format string for the hour values. Default is '%H:%M'.

    Returns:
    - date: list of lists
        The list of date values for each index group.
    - hour: list of lists
        The list of hour values for each index group.
    """
    date = []
    hour = []
    for item in index_grouped:
        date_val = df.iloc[[item[0]], col].index.strftime(date_fmt).to_list()
        hour_val = df.iloc[[item[0]], col].index.strftime(hour_fmt).to_list()
        date.append(date_val)
        hour.append(hour_val)
    return date, hour


def _value_grouped(df, index_grouped, col):
    """Return index_grouped as a list of value lists.

    Args:
        df (pandas.DataFrame): The input DataFrame.
        index_grouped (list): The list of indices to group.
        col (int): The column index to extract values from.

    Returns:
        list: A list of value lists corresponding to the grouped indices.
    """
    value = []
    for item in index_grouped:
        value_val = df.iloc[item, col].to_list()
        value.append(value_val)
    return value


def _dict_grouped(date_list, hour_list, value_list, start=0):
    """
    Join three lists and return as a dictionary.

    Args:
        date_list (list): List of dates.
        hour_list (list): List of hours.
        value_list (list): List of values.
        start (int, optional): Starting index for the dictionary keys. Defaults to 0.

    Returns:
        dict: Dictionary with keys as indices and values as concatenated date, hour, and value.

    """
    item_list = enumerate(zip(date_list, hour_list, value_list), start=start)
    return {i: date + hour + value for i, (date, hour, value) in item_list}


def summary_hourly(
    dataframe,
    column,
    n_hours=24,
    text_date=None,
    return_as_dataframe=True,
    date_format="%Y-%m-%d",
    hour_format="%H:%M",
): # pylint: disable=too-many-arguments,too-many-locals
    """
    Generate a summary of hourly data from a DataFrame.

    Args:
        df (pandas.DataFrame): The input DataFrame.
        column (str): The name of the column containing the hourly data.
        n_hours (int, optional): The number of hours to group together. Defaults to 24.
        text_date (list, optional):
            The list of column names to include in the summary. Defaults to ['date', 'hour'].
        as_df (bool, optional): Whether to return the summary as a DataFrame. Defaults to True.
        date_fmt (str, optional): The date format string. Defaults to '%Y-%m-%d'.
        hour_fmt (str, optional): The hour format string. Defaults to '%H:%M'.

    Returns:
        pandas.DataFrame or dict:
            The summary of hourly data. If `as_df` is True, a DataFrame is returned.
            Otherwise, a dictionary is returned.
    """
    col = dataframe.columns.get_loc(column)
    nrows, _ = dataframe.shape
    results = {}
    text_date = ["date", "hour"] if text_date is None else text_date

    for i in range(0, nrows, n_hours):
        sub_df = dataframe.iloc[i : i + n_hours]
        ix_array = hk73.get_missing_data_indices(~sub_df.iloc[:, col].isna().values)
        ix_grouped = hk73.group_consecutive_elements(ix_array)
        date, hour = _time_grouped(
            sub_df, ix_grouped, col, date_fmt=date_format, hour_fmt=hour_format
        )
        value = _value_grouped(sub_df, ix_grouped, col)
        each_hours = _dict_grouped(date, hour, value, start=i)
        results.update(each_hours)

    if return_as_dataframe:
        columns_name = text_date + [i for i in range(1, n_hours + 1)]
        df_results = pd.DataFrame.from_dict(
            results, orient="index", columns=columns_name
        )
        return df_results
    return results
